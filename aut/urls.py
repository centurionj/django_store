from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('personal_data/', views.PersonalDataView.as_view(), name='personal_data'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('entry/', views.LoginView.as_view(), name='entry'),
    path('change_personal_data/', views.ChangePersonalDataView.as_view(), name='change_personal_data'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('forget_password/', views.ForgetPasswordView.as_view(), name='forget_password'),
    path('verify/<str:verification_token>/', views.verify_account, name='verify_account'),

]
