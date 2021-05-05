from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from items.models import Item
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated {item.name} quantity to {bag[item_id]}')

    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {bag[item_id]} {item.name} to your bag')

    request.session['bag'] = bag
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def adjust_bag(request, item_id):

    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {item.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {item.name} from the bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):

    try:
        item = get_object_or_404(Item, pk=item_id)

        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {item.name} from the bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing the item: {e}')
        return HttpResponse(status=500)
