from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Item
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def all_items(request):
    items = Item.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('items'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            items = items.filter(queries)

    context = {
        'items': items,
        'search_term': query,
    }

    return render(request, 'items/items.html', context)


def item_detail(request, item_id):
    """ A view to show individual item details """

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'items/item_detail.html', context)