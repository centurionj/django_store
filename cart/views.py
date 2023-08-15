from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Cart, CartItem
from products.models import Product


@method_decorator(login_required(login_url='login'), name='dispatch')
class CartView(View):
    """
    отображение корзины и выбор хар-ки товаров
    """

    template_name = 'cart/cart.html'

    def get(self, request):
        cart_items = CartItem.objects.filter(cart__user=request.user)
        context = {'cart_items': cart_items}
        return render(request, self.template_name, context)

    def post(self, request):
        for key, value in request.POST.items():
            if key.startswith('size_') or key.startswith('quantity_'):
                cart_item_id = key.split('_')[1]
                try:
                    cart_item = CartItem.objects.get(id=cart_item_id)
                    if key.startswith('size_'):
                        cart_item.size = value
                    elif key.startswith('quantity_'):
                        cart_item.quantity = value
                    cart_item.save()
                except CartItem.DoesNotExist:
                    pass

        return redirect('cart')


def del_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    redirect_url = request.META.get('HTTP_REFERER', reverse('cart'))

    return HttpResponseRedirect(redirect_url)


@method_decorator(login_required(login_url='login'), name='dispatch')
class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        size_title = request.POST.get('size_title')

        product = get_object_or_404(Product, id=product_id)
        cart, _ = Cart.objects.get_or_create(user=request.user, defaults={'is_active': True})

        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            size=size_title
        )

        cart_item.quantity = cart_item.quantity + 1 if not item_created else 1
        cart_item.price = product.price
        cart_item.save()

        redirect_url = request.META.get('HTTP_REFERER', reverse('personal_data'))

        return HttpResponseRedirect(redirect_url)
