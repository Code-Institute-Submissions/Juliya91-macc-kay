from django.shortcuts import get_object_or_404
from captures.models import Capture


def cart_contents(request):

    cart_items = []
    total = 0
    capture_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            capture = get_object_or_404(Capture, pk=item_id)
            total += item_data * capture.price
            capture_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'capture': capture,
            })
        else:
            capture = get_object_or_404(Capture, pk=item_id)
            for option, quantity in item_data['items_by_option'].items():
                total += quantity * capture.price
                capture_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'capture': capture,
                    'option': option,
                })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'capture_count': capture_count,
        'grand_total': grand_total,
    }

    return context
