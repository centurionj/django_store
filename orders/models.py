from django.db import models
from django.core.validators import MinValueValidator

from products.models import Product
from aut.models import User

class Order(models.Model):
    STATUS_CHOICES = (
        ('processing', 'Обработка'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('canceled', 'Отменен'),
    )

    OPTIONS_CHOICES = (
        ('standard', 'По городу'),
        ('express', 'В регионы'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField('Цена',max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    status = models.CharField('Статус',max_length=100, choices=STATUS_CHOICES)
    options = models.CharField('Доставка',max_length=100, choices=OPTIONS_CHOICES)
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = 'Заказ'
        verbose_name = 'Заказы'
        ordering = ['date_created']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField('Размер', max_length=10, null=True)
    quantity = models.IntegerField('Количество', validators=[MinValueValidator(1)])

    class Meta:
        verbose_name_plural = 'Деталь заказа'
        verbose_name = 'Детали заказа'
        ordering = ['order']

