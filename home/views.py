from django.shortcuts import render
from testimonials.models import Testimonial


def index(request):
    """ index page view """
    testimonials = Testimonial.objects.filter(is_approved=True)[:5]
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'home/index.html', context)


def handler404(request, exception):
    return render(request, '404.html', status=404)


def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')
