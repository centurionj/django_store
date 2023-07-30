from django.urls import path
from . import views

urlpatterns = [
    path('remove_favorite/<int:product_id>/', views.remove_favorite, name='remove_favorite'),
    path('add_product_to_favorite/<int:product_id>', views.add_product_to_favorite, name='add_product_to_favorite'),
]
