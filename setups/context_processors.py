from .models import Logo, Photo, Text

def setup(request):
    """
    Контекстный процессор возвращает словарь с логотипом, фотками и текстом для страниц сайта.

    :param request: Объект запроса.
    :return: Словарь с данными для использования в шаблоне.
    """

    # логотип
    logo = Logo.objects.first()
    logo_url = None
    if logo:
        logo_url = logo.image.url

    # фотки
    men = Photo.objects.filter(status='men')
    men_base = Photo.objects.filter(status='men_base')
    women = Photo.objects.filter(status='women')
    women_base = Photo.objects.filter(status='women_base')
    about = Photo.objects.filter(status='about')

    # текст
    ship_info = Text.objects.filter(status='ship')
    return_info = Text.objects.filter(status='return')
    payment_info = Text.objects.filter(status='payment')
    contacts_info = Text.objects.filter(status='contacts')
    about_info = Text.objects.filter(status='about')

    return {
        'logo_url': logo_url,
        'men': men,
        'men_base': men_base,
        'women': women,
        'women_base': women_base,
        'about': about,
        'ship_info': ship_info if ship_info else None,
        'return_info': return_info if return_info else None,
        'payment_info': payment_info if payment_info else None,
        'contacts_info': contacts_info if contacts_info else None,
        'about_info': about_info if about_info else None
    }
