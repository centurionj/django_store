from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField('Адрес',max_length=100)
    phone_number = models.CharField('Телефон',max_length=20)
    ready_to_spam = models.BooleanField('Подписка на рассылку', default=False)
    verification_token = models.CharField(max_length=255, blank=True, null=True)
    is_verify = models.BooleanField('Подтвержденный аккаунт', null=True, default=False)
    