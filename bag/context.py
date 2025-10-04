from decimal import Decimal
from django.conf import settings
from classes.models import Class as Product
from django.shortcuts import get_object_or_404

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    class_count = product_count

    context = {
        'bag_items': bag_items,
        'class_count': class_count,
        'total': total,
    }

    return context