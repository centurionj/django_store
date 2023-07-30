from django.shortcuts import render, redirect
from django.views import View
from rest_framework.generics import get_object_or_404

from aut.models import UserProfile
from cart.models import Cart
from .models import Order, OrderItem
from cart.context_processors import cart_context
from .tasks import send_check_task


class MakeOrderView(View):
    """
    создание заказа и оплата
    """

    template_name = 'orders/make_order.html'

    def get_context_data(self):
        user = self.request.user
        profile = UserProfile.objects.filter(user=user).first()

        return {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_number': profile.phone_number,
            'address': profile.address,
        }

    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request):
        cart = get_object_or_404(Cart, user=request.user, is_active=True)
        order_status = 'processing'
        order_options = request.POST.get('options')

        cart_context_data = cart_context(request)
        total_price = cart_context_data['total_price']
        cart_items = cart_context_data['cart_items']

        order = Order.objects.create(user=request.user, total_price=total_price,
                                     status=order_status, options=order_options)

        order_items = [OrderItem(order=order, product=item.product,
                                 quantity=item.quantity, size=item.size)
                       for item in cart_items]

        OrderItem.objects.bulk_create(order_items)

        send_check_task.delay(request.user.email, order.id, total_price)

        cart.products.clear()
        cart.save()

        return redirect('success')


def success(request):
    return render(request, 'orders/success.html')
