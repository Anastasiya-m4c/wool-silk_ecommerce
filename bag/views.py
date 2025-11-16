from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.urls import reverse
from classes.models import Class


def view_bag(request):
    """ A view to return the shopping bag page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    
    my_class = get_object_or_404(Class, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    current_quantity = bag.get(item_id, 0)
    total_quantity = current_quantity + quantity

    if my_class.manually_fully_booked:
        messages.error(request, f'Sorry, {my_class.name} is currently fully booked.')
        return redirect(redirect_url)
    
    spots_remaining = my_class.get_spots_remaining()
    if total_quantity > spots_remaining:
        if current_quantity > 0:
            messages.error(
                request,
                f'Sorry, only {spots_remaining} spot(s) available. You already have {current_quantity} in your bag.'
            )
        else:
            messages.error(request, f'Sorry, only {spots_remaining} spot(s) available for {my_class.name}.')
        return redirect(redirect_url)
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {my_class.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {my_class.name} to your bag')
    
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


@require_POST
def adjust_bag(request, item_id):
    """Adjust the quantity """
    
    my_class = get_object_or_404(Class, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    
    if quantity > 0:
        if my_class.manually_fully_booked:
            messages.error(request, f'{my_class.name} is now fully booked.')
            return redirect(reverse('view_bag'))
        
        spots_remaining = my_class.get_spots_remaining()
        current_quantity = bag.get(item_id, 0)
        actual_available = spots_remaining + current_quantity
        
        if quantity > actual_available:
            messages.error(request, f'Sorry, only {actual_available} spot(s) available for {my_class.name}.')
            return redirect(reverse('view_bag'))
        
        bag[item_id] = quantity
        messages.success(request, f'Updated {my_class.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {my_class.name} from your bag')
    
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """
    
    my_class = get_object_or_404(Class, pk=item_id)
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id, None)
        messages.success(request, f'Removed {my_class.name} from your bag')
        
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e: 
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

