from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item


def bag_contents(request):

    bag_items = []
    total = 0
    item_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        item = get_object_or_404(Item, pk=item_id)
        total += quantity * item.price
        item_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'item': item,
        })

    if total < settings.DISCOUNT_THRESHOLD:
        discount_delta = settings.DISCOUNT_THRESHOLD - total
        discount = 0
    else:
        discount = total * Decimal(settings.DISCOUNT_PERCENTAGE / 100)
        discount_delta = 0

    grand_total = total - discount

    context = {
        'bag_items': bag_items,
        'total': total,
        'item_count': item_count,
        'discount': discount,
        'grand_total': grand_total,
        'discount_delta': discount_delta,
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
    }

    return context
