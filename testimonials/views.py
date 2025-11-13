from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm
from checkout.models import Order

@login_required
def submit_testimonial(request):
    # Check if user has made a purchase
    has_purchased = Order.objects.filter(email=request.user.email).exists()
    
    if not has_purchased:
        messages.error(request, 'You must make a purchase before submitting a testimonial.')
        return redirect('home')
    
    # Check if user already submitted a testimonial
    existing = Testimonial.objects.filter(user=request.user).exists()
    if existing:
        messages.info(request, 'You have already submitted a testimonial.')
        return redirect('testimonials')
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Thank you! Your testimonial has been submitted and is awaiting approval.')
            return redirect('home')
    else:
        form = TestimonialForm()
    
    context = {'form': form}
    return render(request, 'testimonials/submit_testimonial.html', context)

def testimonials_list(request):
    testimonials = Testimonial.objects.filter(is_approved=True)
    context = {'testimonials': testimonials}
    return render(request, 'testimonials/testimonials_list.html', context)

