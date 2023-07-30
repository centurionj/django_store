from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Favorite
from products.models import Product

@login_required(login_url='login')
def add_product_to_favorite(request, product_id):
    try:
        favorite, _ = Favorite.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product, id=product_id)

        favorite.products.add(product)

        redirect_url = request.META.get('HTTP_REFERER', reverse('catalog'))

        return HttpResponseRedirect(redirect_url)

    except (Favorite.DoesNotExist, Product.DoesNotExist):
        return render(request, 'main/400.html', {'error': 'Что-то пошло не так'}, status=400)


def remove_favorite(request, product_id):
    if request.user.is_authenticated:
        favorite = get_object_or_404(Favorite, user=request.user)
        product = get_object_or_404(Product, id=product_id)
        favorite.products.remove(product)

        redirect_url = request.META.get('HTTP_REFERER', reverse('personal_data'))

        return HttpResponseRedirect(redirect_url)
