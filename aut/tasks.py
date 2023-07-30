import uuid

from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse

from aut.models import UserProfile


@shared_task
def send_verification_email_task(user_id, scheme, host):
    """
    отправка письма для подтверждения аккаунта
    """

    try:
        user = UserProfile.objects.get(user_id=user_id).user

        verification_token = str(uuid.uuid4())
        verification_link = reverse(
            'verify_account',
            kwargs={'verification_token': verification_token})

        verification_url = f"{scheme}://{host}{verification_link}"

        profile = user.userprofile
        profile.verification_token = verification_token
        profile.save()

        subject = 'Подтверждение аккаунта'
        message = f'Для подтверждения аккаунта перейдите по ссылке: {verification_url}'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])
    except UserProfile.DoesNotExist:
        pass

@shared_task
def send_one_time_password_task(email, one_time_password):
    subject = 'Разовый пароль для входа на сайт'
    message = f'Ваш разовый пароль: {one_time_password}\nНе забудьте сразу после входа сменить пароль.'
    recipient_list = [email]
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
