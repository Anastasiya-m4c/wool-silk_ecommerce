from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_POST
from django.urls import reverse

# Create your views here.

def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


@require_POST
def adjust_bag(request, item_id):
    """Adjust the quantity """
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id, None)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception:
        return HttpResponse(status=500)