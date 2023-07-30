from django.shortcuts import get_object_or_404, redirect

from . models import PromoCode
from cart.models import Cart


def use_promo(request):
    """
    промокоды для скидки
    """

    promo_code = request.POST.get('promo_code')

    discount_code = get_object_or_404(PromoCode, code=promo_code)

    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.filter(is_promo_used=False)

    for cart_item in cart_items:
        cart_item.price -= cart_item.price * (discount_code.discount / 100)
        cart_item.is_promo_used = True
        cart_item.save()

    return redirect('cart')
