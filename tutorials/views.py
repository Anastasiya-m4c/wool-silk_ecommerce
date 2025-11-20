from django.shortcuts import render


def tutorials_list(request):
    """ A view to show tutorials coming soon page """
    return render(request, 'tutorials/tutorials.html')

