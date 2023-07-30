from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('cart/', include('cart.urls')),
    path('news/', include('news.urls')),
    path('catalog/', include('products.urls')),
    path('login/', include('aut.urls')),
    path('order/', include('orders.urls')),
    path('favourite/', include('favourites.urls')),
    path('promocodes/', include('promocodes.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.handler404'
handler400 = 'main.views.handler400'
