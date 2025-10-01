from django.shortcuts import render
from .models import Class

# Create your views here.

def all_classes(request):
    """ A view to show all classes """

    classes = Class.objects.all()
    context = {
        'classes': classes,
    }
    
    return render(request, 'classes/classes.html', context)