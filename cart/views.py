from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified capture to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    option = None
    if 'capture_option' in request.POST:
        option = request.POST['capture_option']
    cart = request.session.get('cart', {})

    if option:
        if item_id in list(cart.keys()):
            if option in cart[item_id]['items_by_option'].keys():
                cart[item_id]['items_by_option'][option] += quantity
            else:
                cart[item_id]['items_by_option'][option] = quantity
        else:
            cart[item_id] = {'items_by_option': {option: quantity}}

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of specified capture to the specified amount """

    quantity = int(request.POST.get('quantity'))
    option = None
    if 'capture_option' in request.POST:
        option = request.POST['capture_option']
    cart = request.session.get('cart', {})

    if option:
        if quantity > 0:
            cart[item_id]['items_by_option'][option] = quantity
        else:
            del cart[item_id]['items_by_option'][option]
            if not cart[item_id]['items_by_option']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        option = None
        if 'capture_option' in request.POST:
            option = request.POST['capture_option']
        cart = request.session.get('cart', {})

        if option:
            del cart[item_id]['items_by_option'][option]
            if not cart[item_id]['items_by_option']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
