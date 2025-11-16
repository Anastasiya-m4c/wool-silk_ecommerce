from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.db import transaction
from .forms import OrderForm
from .models import Order, OrderLineItem
from classes.models import Class
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.context import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        for item_id, quantity in list(bag.items()):
            try:
                class_obj = Class.objects.get(id=item_id)
                
                if class_obj.manually_fully_booked:
                    messages.error(
                        request,
                        f'Sorry, {class_obj.name} is now fully booked and has been removed from your bag.'
                    )
                    bag.pop(item_id)
                    request.session['bag'] = bag
                    return redirect(reverse('view_bag'))
                
                spots_available = class_obj.get_spots_remaining()
                
                if quantity > spots_available:
                    if spots_available > 0:
                        bag[item_id] = spots_available
                        request.session['bag'] = bag
                        messages.warning(
                            request,
                            f'{class_obj.name} only has {spots_available} spot(s) available. '
                            f'Quantity adjusted in your bag.'
                        )
                        return redirect(reverse('view_bag'))
                    else:
                        bag.pop(item_id)
                        request.session['bag'] = bag
                        messages.error(
                            request,
                            f'{class_obj.name} is now fully booked and has been removed from your bag.'
                        )
                        return redirect(reverse('view_bag'))
                        
            except Class.DoesNotExist:
                messages.error(request, 'A class in your bag no longer exists.')
                bag.pop(item_id)
                request.session['bag'] = bag
                return redirect(reverse('view_bag'))

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # AI generated code- Wrap order creation in transaction with locking
            try:
                with transaction.atomic():
                    order = order_form.save(commit=False)
                    pid = request.POST.get('client_secret').split('_secret')[0]
                    order.stripe_pid = pid
                    order.original_bag = json.dumps(bag)
                    order.save()
                    
                    for item_id, item_data in bag.items():
                        #AI generated code - Lock the class row to prevent race conditions
                        product = Class.objects.select_for_update().get(id=item_id)
                        
                        #AI generated code - Final availability check under lock
                        if product.manually_fully_booked:
                            raise ValueError(f'{product.name} is now fully booked')
                        
                        if isinstance(item_data, int):
                            if not product.has_available_spots(item_data):
                                raise ValueError(f'{product.name} does not have enough spots available')
                            
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=item_data,
                            )
                            order_line_item.save()
                            
            except Class.DoesNotExist:
                messages.error(request, (
                    "One of the classes in your bag wasn't found in our database. "
                    "Please call us for assistance!")
                )
                return redirect(reverse('view_bag'))
            except ValueError as e:
                # AI generated code - Availability changed during checkout
                messages.error(request, f'Sorry, {str(e)}. Please check your bag and try again.')
                return redirect(reverse('view_bag'))
            except Exception as e:
                messages.error(request, 'An error occurred while processing your order. Please try again.')
                return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('classes'))

        for item_id, quantity in list(bag.items()):
            try:
                class_obj = Class.objects.get(id=item_id)
                
                if class_obj.manually_fully_booked:
                    messages.error(
                        request,
                        f'{class_obj.name} is now fully booked and has been removed from your bag.'
                    )
                    bag.pop(item_id)
                    request.session['bag'] = bag
                    return redirect(reverse('view_bag'))
                
                spots_available = class_obj.get_spots_remaining()
                if quantity > spots_available:
                    if spots_available > 0:
                        bag[item_id] = spots_available
                        request.session['bag'] = bag
                        messages.warning(
                            request,
                            f'{class_obj.name} only has {spots_available} spot(s) available. '
                            f'Quantity adjusted.'
                        )
                    else:
                        bag.pop(item_id)
                        request.session['bag'] = bag
                        messages.error(
                            request,
                            f'{class_obj.name} is fully booked and has been removed.'
                        )
                    return redirect(reverse('view_bag'))
                    
            except Class.DoesNotExist:
                messages.error(request, 'A class in your bag no longer exists.')
                bag.pop(item_id)
                request.session['bag'] = bag
                return redirect(reverse('view_bag'))

        current_bag = bag_contents(request)
        total = current_bag['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_email': order.email,
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! Your order number is {order_number}. '
                              f'A confirmation email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

