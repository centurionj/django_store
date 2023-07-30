from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.views.generic import DetailView
from django.core.paginator import Paginator

from urllib.parse import urlencode

from products.tasks.tasks import perform_parsing, deserialize_json
from .models import Product


class CatalogView(View):
    """
    отображение каталога и работа фильтрации
    """

    def get(self, request):
        sizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL']
        selected_sizes = [size for size in sizes if request.GET.get('size_' + size)]

        filters = {
            'gender': request.GET.get('gender'),
            'brand__slug': request.GET.get('brand'),
            'category__slug': request.GET.get('category'),
            'sizes__title__in': selected_sizes,
            'price__gte': request.GET.get('min_price'),
            'price__lte': request.GET.get('max_price'),
        }

        products = Product.objects.filter(**{k: v for k, v in filters.items() if v})

        if request.GET.get('sale'):
            products = Product.objects.filter(is_sale=True)

        paginator = Paginator(products, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        params = request.GET.copy()
        if 'page' in params:
            del params['page']
        encoded_params = urlencode(params)

        context = {
            'page_obj': page_obj,
            'sizes': sizes,
            'selected_sizes': selected_sizes,
            'min_price': filters['price__gte'],
            'max_price': filters['price__lte'],
            'encoded_params': encoded_params,
            'base_url': request.path,
            'gender': filters['gender'],
            'brand': filters['brand__slug'],
        }

        return render(request, 'products/catalog.html', context)


class ProductDetailView(DetailView):
    """
    детальный просмотр товара
    """

    model = Product
    template_name = 'products/product_detail_view.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product = context[self.context_object_name]

        similar_products = Product.objects.filter(brand=product.brand).exclude(pk=product.pk)

        context['similar_products'] = similar_products
        context['sizes'] = product.sizes.all()

        return context


def parsing(request):
    perform_parsing.delay()
    return redirect('admin:index')

def fill_bd(request):
    """
    заполнение данными из json. замена ручного добавления
    """

    deserialize_json.delay()
    return HttpResponse(f"Товары из JSON успешно добавлены в базу данных")
