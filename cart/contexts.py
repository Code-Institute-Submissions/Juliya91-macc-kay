def cart_contents(request):

    cart_items = []
    total = 0
    captures_count = 0

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'captures_count': captures_count,
        'grand_total': grand_total,
    }

    return context
