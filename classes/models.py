from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    deposit = models.DecimalField(max_digits=6, decimal_places=2,
                                  null=True, blank=True)
    # rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    # fully_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        # return f"self.name" ({self.start_time.strftime('%d/%m/%Y')}) 
