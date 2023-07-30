from django.db import models
from django.core.validators import MinValueValidator


class PromoCode(models.Model):
    code = models.CharField('Промокод', max_length=20, unique=True)
    description = models.CharField('Описание', max_length=100, blank=True, null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name_plural = 'Промокод'
        verbose_name = 'Промокоды'
        ordering = ['code']

    def __str__(self):
        return self.code
