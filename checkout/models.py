import uuid
from decimal import Decimal
from django.db import models
from django.db.models import Sum
from classes.models import Class


class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True, editable=False)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=40)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))

    def _generate_order_number(self):
        """Generate a random, unique order number using UUID"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """Update order total each time a line item is added/updated"""
        total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or Decimal("0.00")
        self.order_total = total
        self.save(update_fields=['order_total'])

    def save(self, *args, **kwargs):
        """Set the order number if it hasn't been set already."""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems'
    )
    product = models.ForeignKey(
        Class, null=False, blank=False,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    lineitem_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        """Set the lineitem total and update the parent order total."""
        self.lineitem_total = (self.product.price or Decimal("0.00")) * self.quantity
        super().save(*args, **kwargs)
        self.order.update_total()

    def __str__(self):
        return f'{self.product.name} × {self.quantity} on order {self.order.order_number}'
