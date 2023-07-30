from django.shortcuts import render

from products.models import Product


def index(request):
    men_products = Product.objects.filter(gender='M').prefetch_related('brand', 'category', 'images')
    women_products = Product.objects.filter(gender='F').prefetch_related('brand', 'category', 'images')

    context = {
        'men_products': men_products if men_products.exists() else [],
        'women_products': women_products if women_products.exists() else [],
    }

    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def support(request):
    return render(request, 'main/support.html')

def handler404(request, *args, **argv):
    response = render(request, 'main/404.html')
    response.status_code = 404
    return response

def handler400(request, exception, *args, **argv):
    context = {
        'error': str({exception}),
    }

    response = render(request, 'main/400.html', context=context)
    response.status_code = 400
    return response
