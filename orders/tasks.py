from celery import shared_task

from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_check_task(email, order_id, total_price):
    """
    отправка чека на почту юзеру и админу
    """

    user_subject = f'Ваш заказ {order_id} успешно оплачен!'
    user_message = (
        f'Уведомление об оплате заказа \n'
        f'{order_id} \n\n'
        f'{total_price} \nRUB \n\n'
        f'Следите за статусом заказа в личном кабинете http://0.0.0.0/login/personal_data/'
    )
    recipient_list = [email]

    send_mail(
        user_subject,
        user_message,
        settings.EMAIL_HOST_USER,
        recipient_list
    )

    admin_subject = 'Чек'
    admin_message = f'Уведомление об оплате заказа \n {order_id} \n\n Стоимостью: {total_price} \nRUB'

    send_mail(admin_subject, admin_message, settings.EMAIL_HOST_USER, ['ostory.shop@mail.ru'])
