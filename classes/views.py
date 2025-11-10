from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Class
from .forms import ClassForm
from django.contrib import messages

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
    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added class!')
            return redirect(reverse('classes'))
        else:
            messages.error(request, 'Failed to add class. Please ensure the form is valid.')
    else:
        form = ClassForm()

    form = ClassForm()
    template = 'classes/add_class.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

def edit_class(request, class_id):
    """ A view to edit a class in the store """
    classes = get_object_or_404(Class, pk=class_id)
    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES, instance=classes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated class!')
            return redirect(reverse('class_detail', args=[classes.id]))
        else:
            messages.error(request, 'Failed to update class. Please ensure the form is valid.')
    else:
        form = ClassForm(instance=classes)
        messages.info(request, f'You are editing {classes.name}')

    template = 'classes/edit_class.html'
    context = {
        'form': form,
        'class': classes,
    }
    return render(request, template, context)