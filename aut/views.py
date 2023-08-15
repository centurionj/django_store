from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.crypto import get_random_string
from rest_framework.views import APIView
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import UserProfile
from .forms import ForgetPasswordForm
from .tasks import send_verification_email_task, send_one_time_password_task
from orders.models import Order, OrderItem


class PersonalDataView(LoginRequiredMixin, View):
    login_url = 'login'  # Указываем URL страницы входа

    """
    рендер личного кабинета со всеми данными и опциями (заказ, лайк и тд)
    """
    def get_context_data(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)

        context = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'address': profile.address,
            'phone_number': profile.phone_number,
            'is_verify': profile.is_verify,
        }

        orders = Order.objects.filter(user=request.user).order_by('-date_created')
        order_items = OrderItem.objects.filter(order__in=orders)

        if not orders.exists():
            orders = []
            order_items = []

        context.update({
            'orders': orders,
            'order_items': order_items,
        })

        return context

    def get(self, request):
        context = self.get_context_data(request)
        return render(request, 'aut/personal_data.html', context=context)

class RegistrationView(APIView):
    """
    регистрация юзера
    """

    def post(self, request):
        data = request.data

        UserModel = get_user_model()

        if UserModel.objects.filter(email=data['email']).exists():
            return render(
                request,
                'main/400.html',
                {'error': 'Пользователь с такой электронной почтой уже существует'},
                status=400
            )

        user = UserModel.objects.create_user(
            username=data['email'],
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )

        UserProfile.objects.create(
            user=user,
            address=data['address'],
            phone_number=data['phone_number']
        )

        user = authenticate(request, username=data['email'], password=data['password'])
        login(request, user)

        send_verification_email_task.delay(
            user.id,
            request.scheme,
            request.get_host()
        )

        return redirect('personal_data')


def verify_account(request, verification_token):
    user_profile = get_object_or_404(UserProfile, verification_token=verification_token)
    user_profile.is_verify = True
    user_profile.verification_token = None
    user_profile.save()
    return redirect('personal_data')


class LoginView(APIView):
    """
    вход в аккаунт
    """

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('personal_data')
        return render(request, 'aut/login.html')

    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None and user.is_authenticated:
            login(request, user)
            return redirect('personal_data')

        error_message = 'Неправильная электронная почта или пароль'
        return render(request, 'main/400.html', {'error': error_message}, status=400)


class ForgetPasswordView(APIView):
    """
    восстановление пароля через одноразовый пароль
    """

    def get(self, request):
        form = ForgetPasswordForm()
        return render(request, 'aut/forget_password.html', {'form': form})

    def post(self, request):
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = get_object_or_404(User, email=email)

            one_time_password = get_random_string(length=10)

            user.set_password(one_time_password)
            user.save()

            # Вызываем задачу Celery для отправки разового пароля
            send_one_time_password_task.delay(email, one_time_password)

            return redirect('login')
        else:
            return render(request, 'aut/forget_password.html', {'form': form})


class ChangePasswordView(APIView):
    """
    смена пароля через рандомный на почту
    """

    def post(self, request, *args, **kwargs):
        user = request.user
        new_password = request.data.get('new_password')

        if user.check_password(new_password):
            error_message = 'Новый пароль не должен совпадать со старым'
            return render(request, 'main/400.html', {'error': error_message}, status=400)

        user.set_password(new_password)
        user.save()

        login(request, user)

        return redirect('personal_data')


class ChangePersonalDataView(APIView):
    """
    изменение данных в лк
    """
    def post(self, request):
        user = request.user
        profile = user.userprofile

        # Получение новых значений из запроса
        user.first_name = request.data.get('first_name')
        user.last_name = request.data.get('last_name')
        profile.phone_number = request.data.get('phone_number')
        profile.address = request.data.get('address')

        user.save(update_fields=['first_name', 'last_name', 'email'])
        profile.save(update_fields=['phone_number', 'address'])

        redirect_url = request.META.get('HTTP_REFERER', reverse('personal_data'))

        return HttpResponseRedirect(redirect_url)
