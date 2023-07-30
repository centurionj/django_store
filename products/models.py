from django.db import models
from django.core.validators import MinValueValidator
from autoslug import AutoSlugField

from mptt.models import MPTTModel, TreeForeignKey


class Brand(MPTTModel):
    name = models.CharField('Брэнд', max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = AutoSlugField(populate_from='name', unique=True, editable=False)
    categories = models.ManyToManyField('Category', related_name='brands', blank=True)

    class Meta:
        verbose_name_plural = 'Брэнды'
        verbose_name = 'Брэнд'
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField('Категория', max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = AutoSlugField(populate_from='name', unique=True, editable=False)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']

    def __str__(self):
        return self.name


class Size(models.Model):
    title = models.CharField('Размер', max_length=5, null=True)

    class Meta:
        verbose_name_plural = 'Размер'
        verbose_name = 'Размеры'

    def __str__(self):
        return self.title


class Product(models.Model):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )

    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    image = models.URLField(null=True, blank=True)
    is_sale = models.BooleanField('Скидка', default=False)
    slug = AutoSlugField(populate_from='name', unique=True, editable=False)
    gender = models.CharField('Пол', max_length=1, null=True, blank=True, choices=GENDER_CHOICES)
    sizes = models.ManyToManyField(Size, related_name='products')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Фото'
        verbose_name = 'Фото'

    def __str__(self):
        return str(self.image)
