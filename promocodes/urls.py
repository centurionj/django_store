from django.urls import path
from . import views

urlpatterns = [
    path('', views.use_promo, name='use_promo'),
]
