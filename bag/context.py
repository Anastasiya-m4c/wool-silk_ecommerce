from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    
    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
    }

    return context