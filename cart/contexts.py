from django.shortcuts import get_object_or_404
from captures.models import Captures


def cart_contents(request):

    cart_items = []
    total = 0
    captures_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        captures = get_object_or_404(Captures, pk=item_id)
        total += quantity * captures.price
        captures_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'captures': captures,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'captures_count': captures_count,
        'grand_total': grand_total,
    }

    return context
