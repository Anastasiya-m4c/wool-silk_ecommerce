from django.db import models
from django.db.models import Sum


class Class(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    image = models.ImageField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    location = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    max_capacity = models.IntegerField(
        default=10,
        help_text="Maximum number of attendees"
    )

    # Manual override for admin
    manually_fully_booked = models.BooleanField(
        default=False,
        help_text=(
            "Check this to manually mark the class as fully "
            "booked (e.g., for bookings received via "
            "phone/email)"
        )
    )

    def __str__(self):
        return self.name

    def get_total_bookings(self):
        """
        Get total confirmed bookings by summing OrderLineItem
        quantities. Import inside method to avoid circular
        import.
        """
        from checkout.models import OrderLineItem

        total = OrderLineItem.objects.filter(
            product=self
        ).aggregate(
            total_quantity=Sum('quantity')
        )['total_quantity']

        return total or 0

    def get_spots_remaining(self):
        """Calculate remaining spots"""
        if self.manually_fully_booked:
            return 0
        return max(
            0,
            self.max_capacity - self.get_total_bookings()
        )

    def is_fully_booked(self):
        """Check if fully booked (manually or by capacity)"""
        if self.manually_fully_booked:
            return True
        return self.get_spots_remaining() <= 0

    def has_available_spots(self, requested_quantity=1):
        """
        Check if enough spots available for requested quantity.
        Useful for validation before adding to bag.
        """
        if self.manually_fully_booked:
            return False
        return (
            self.get_spots_remaining() >= requested_quantity
        )

    @property
    def availability_status(self):
        """Return booking status for display"""
        if self.manually_fully_booked:
            return "Fully Booked (Manual)"

        spots = self.get_spots_remaining()
        if spots <= 0:
            return "Fully Booked"
        elif spots <= 3:
            return f"Only {spots} spot(s) left!"
        else:
            return f"{spots} spots available"

    @property
    def booking_status_detail(self):
        """Detailed status for admin view"""
        total_booked = self.get_total_bookings()
        if self.manually_fully_booked:
            return (
                f"Manually marked as fully booked "
                f"({total_booked}/{self.max_capacity} "
                f"actual bookings)"
            )
        elif self.is_fully_booked():
            return (
                f"Fully booked by capacity "
                f"({total_booked}/{self.max_capacity})"
            )
        else:
            spots_left = self.get_spots_remaining()
            return (
                f"{total_booked}/{self.max_capacity} booked, "
                f"{spots_left} spot(s) remaining"
            )

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ['start_date', 'start_time']
