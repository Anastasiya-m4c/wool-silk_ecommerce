from django.shortcuts import render
from testimonials.models import Testimonial

def index(request):
    """ index page view """
    testimonials = Testimonial.objects.filter(is_approved=True)[:5]
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'home/index.html', context)

