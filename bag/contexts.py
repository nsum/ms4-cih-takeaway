from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.DISCOUNT_THRESHOLD:
        discount_delta = settings.DISCOUNT_THRESHOLD - total
    else: 
        total = total / Decimal(settings.DISCOUNT_PERCENTAGE / 100)

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount_delta': discount_delta,
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
    }

    return context