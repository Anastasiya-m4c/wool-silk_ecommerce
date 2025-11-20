"""
urls.py' for the 'tutorials' app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutorials_list, name='tutorials'),
]
