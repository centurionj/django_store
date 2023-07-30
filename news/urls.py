from django.urls import path

from . import views


urlpatterns = [
    path('', views.update_spam_preference, name='spam'),
]
