from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Send email notification to admin
            try:
                send_mail(
                    subject=f'New Contact Form Submission: {contact.subject}',
                    message=f'Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                # Log error but don't break the form submission
                print(f"Email error: {e}")
            
            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
