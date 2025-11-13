from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonials_list, name='testimonials'),
    path('submit/', views.submit_testimonial, name='submit_testimonial'),
]