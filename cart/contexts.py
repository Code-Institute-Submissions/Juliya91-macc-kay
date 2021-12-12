from django.shortcuts import get_object_or_404
from captures.models import Capture


def cart_contents(request):

    cart_items = []
    total = 0
    capture_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        capture = get_object_or_404(Capture, pk=item_id)
        total += quantity * capture.price
        capture_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'capture': capture,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'capture_count': capture_count,
        'grand_total': grand_total,
    }

    return context
