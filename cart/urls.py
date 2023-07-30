from django.urls import path

from . import views

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('remove/<int:cart_item_id>/', views.del_cart_item, name='del_cart_item'),
    path('add_item_to_cart/', views.AddToCartView.as_view(), name='add_item_to_cart'),
]
