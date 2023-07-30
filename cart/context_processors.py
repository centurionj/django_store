import logging

from .models import Cart

def cart_context(request):
    """
    отображение элементов корзины в панели навигации
    """

    cart_items = []
    total_price = 0
    item_count = 0

    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_items = cart.cartitem_set.all()
            total_price = sum(item.price * item.quantity for item in cart_items)
            item_count = sum(item.quantity for item in cart_items)

        except Exception as e:
            logging.exception(e)

    return {
        'cart_items': cart_items,
        'total_price': total_price,
        'item_count': item_count,
    }
