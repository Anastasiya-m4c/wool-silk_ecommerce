from django.db import models
from django.contrib.auth.models import User


class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100,
        blank=True,
        default='',
        help_text="This name will be displayed publicly with your testimonial"
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_display_name()} - {self.title}"

    def get_display_name(self):
        """Return name if provided, otherwise 'Anonymous'"""
        return self.name if self.name else "Anonymous"
