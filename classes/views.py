from django.shortcuts import render, get_object_or_404
from .models import Class
from .forms import ClassForm

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

def add_class(request):
    """ A view to add a class to the store """
    form = ClassForm()
    template = 'classes/add_class.html'
    context = {
        'form': form,
    }
    return render(request, template, context)