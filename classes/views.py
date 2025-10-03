from django.shortcuts import render, get_object_or_404
from .models import Class

# Create your views here.

def all_classes(request):
    """ A view to show all classes """

    classes = Class.objects.all()
    context = {
        'classes': classes,
    }

    return render(request, 'classes/classes.html', context)



def class_detail(request, class_id):
    """ A view to show individual class details """

    classes = get_object_or_404(Class, pk=class_id)

    context = {
        'class': classes,
    }
    
    return render(request, 'classes/class_detail.html', context)