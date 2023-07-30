from django.db import models

from products.models import Product
from aut.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    is_active = models.BooleanField('Активность',default=True)

    class Meta:
        verbose_name_plural = 'Корзина'
        verbose_name = 'Корзины'

    def __str__(self):
        return str(self.user)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField('Размер', max_length=10, null=True)
    quantity = models.IntegerField('Количество', null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, null=True)
    is_promo_used = models.BooleanField('Применен промокод', null=True, default=False)

    class Meta:
        verbose_name_plural = 'Элемент корзины'
        verbose_name = 'Элементы корзины'

    def __str__(self):
        return str(self.product)
