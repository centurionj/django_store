from django.urls import path
from . import views


urlpatterns = [
    path('', views.MakeOrderView.as_view(), name='make_order'),
    path('success/', views.success, name='success')
]
