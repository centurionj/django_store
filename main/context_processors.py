from mptt.templatetags.mptt_tags import recursetree

from products.models import Brand, Product, Category

def header(request):
    """
    Контекстный процессор предоставляет данные, которые используются в шаблоне 'base.html'.
    Он возвращает словарь с данными о брендах, категориях и продуктах для мужчин и женщин, а также
    функцию `recursetree` из `mptt` для обхода дерева категорий

    :param request: Объект запроса.
    :return: Словарь с данными для использования в шаблоне.
    """

    brand_list_men = Brand.objects.filter(categories__products__gender='M').distinct().prefetch_related('categories')
    brand_list_women = Brand.objects.filter(categories__products__gender='F').distinct().prefetch_related('categories')

    # Получаем уникальные категории, которые относятся только к мужским товарам
    category_list_men = Category.objects.filter(products__gender='M').distinct()
    # Получаем уникальные категории, которые относятся только к женским товарам
    category_list_women = Category.objects.filter(products__gender='F').distinct()

    sale_products = Product.objects.filter(is_sale=True).prefetch_related('brand', 'category', 'images')

    return {
        'brand_list_men': brand_list_men if brand_list_men.exists() else [],
        'brand_list_women': brand_list_women if brand_list_women.exists() else [],
        'category_list_men': category_list_men if category_list_men.exists() else [],
        'category_list_women': category_list_women if category_list_women.exists() else [],
        'recursetree': recursetree,
        'sale_products': sale_products,
    }
