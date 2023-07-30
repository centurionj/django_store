from .models import Favorite


def favourite_context(request):
    """
    отображение лайкнутых в панели навигации
    """

    favourite_items = []

    if request.user.is_authenticated:
        try:
            favourite = Favorite.objects.get(user=request.user)
            favourite_items = favourite.products.all()
        except Favorite.DoesNotExist:
            pass

    return {
        'favourite_items': favourite_items,
    }
