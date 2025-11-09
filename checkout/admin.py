from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdmin,)

    readonly_fields = ('order_number', 'date', 'order_total')

    fields = (
        'order_number', 'user_profile', 'date' 'full_name', 'email', 'phone_number',
        'country', 'postcode', 'town_or_city', 'street_address1',
        'street_address2', 'date', 'order_total', 'original_bag', 
        'stripe_pid',
    )

    list_display = (
        'order_number', 'full_name', 'date', 'order_total',
    )

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
