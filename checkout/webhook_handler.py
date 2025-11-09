from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from classes.models import Class
from profiles.models import UserProfile

import json
import stripe
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )      

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Retrieve the charge and billing details
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        billing_details = stripe_charge.billing_details
        order_total = round(stripe_charge.amount / 100, 2)

        # Extract billing fields safely (may be None)
        b_name = billing_details.name if getattr(billing_details, 'name', None) else None
        b_email = billing_details.email if getattr(billing_details, 'email', None) else None
        b_phone = billing_details.phone if getattr(billing_details, 'phone', None) else None

        b_address = getattr(billing_details, 'address', {}) or {}
        b_country = b_address.get('country') if isinstance(b_address, dict) else None
        b_postal_code = b_address.get('postal_code') if isinstance(b_address, dict) else None
        b_city = b_address.get('city') if isinstance(b_address, dict) else None
        b_line1 = b_address.get('line1') if isinstance(b_address, dict) else None
        b_line2 = b_address.get('line2') if isinstance(b_address, dict) else None

        # Normalize blank strings to None
        def clean(val):
            return val if val not in (None, '') else None

        b_name = clean(b_name)
        b_email = clean(b_email)
        b_phone = clean(b_phone)
        b_country = clean(b_country)
        b_postal_code = clean(b_postal_code)
        b_city = clean(b_city)
        b_line1 = clean(b_line1)
        b_line2 = clean(b_line2)

        # Get user profile if logged in
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            try:
                profile = UserProfile.objects.get(user__username=username)
            except UserProfile.DoesNotExist:
                pass

        # Try to find an existing order (retry loop)
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=b_name or '',
                    email__iexact=b_email or '',
                    phone_number__iexact=b_phone or '',
                    country__iexact=b_country or '',
                    postcode__iexact=b_postal_code or '',
                    town_or_city__iexact=b_city or '',
                    street_address1__iexact=b_line1 or '',
                    street_address2__iexact=b_line2 or '',
                    order_total=order_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200
            )

        # Create the order if it doesn't exist
        order = None
        try:
            order = Order.objects.create(
                full_name=b_name,
                user_profile=profile,
                email=b_email,
                phone_number=b_phone,
                country=b_country,
                postcode=b_postal_code,
                town_or_city=b_city,
                street_address1=b_line1,
                street_address2=b_line2,
                order_total=order_total,
                original_bag=bag,
                stripe_pid=pid,
            )

            # Create order line items
            for item_id, quantity in json.loads(bag).items():
                product = Class.objects.get(id=item_id)
                qty = quantity if isinstance(quantity, int) else quantity.get('quantity', 1)
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=qty,
                )
                order_line_item.save()

            # Update profile default info if save_info was checked
            if profile and save_info == 'true':
                profile.default_phone_number = b_phone
                profile.default_country = b_country
                profile.default_postcode = b_postal_code
                profile.default_town_or_city = b_city
                profile.default_street_address1 = b_line1
                profile.default_street_address2 = b_line2
                profile.save()

        except Exception as e:
            if order:
                order.delete()
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: {e}',
                status=500
            )
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

