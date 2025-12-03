from django.urls import path
from . import views


urlpatterns = [
    path('', views.testimonials_list, name='testimonials'),
    path('submit/', views.submit_testimonial, name='submit_testimonial'),
    path(
        'manage/',
        views.manage_testimonials,
        name='manage_testimonials'
    ),
    path(
        'approve/<int:testimonial_id>/',
        views.approve_testimonial,
        name='approve_testimonial'
    ),
    path(
        'delete/<int:testimonial_id>/',
        views.delete_testimonial,
        name='delete_testimonial'
    ),
]