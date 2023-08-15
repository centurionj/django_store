from django.db import models


class Logo(models.Model):
    image = models.FileField('Логотип', null=True, blank=True)

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'

    def __str__(self):
        return str(self.image.name)


class Photo(models.Model):
    STATUS_CHOICES = (
        ('men', 'Мужские образы'),
        ('men_base', 'Мужское на главной'),
        ('women', 'Женские образы'),
        ('women_base', 'Женское на главной'),
        ('about', 'О нас'),
    )

    image = models.FileField('Фото')
    status = models.CharField('Раздел сайта', max_length=100, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return self.status.title()


class Text(models.Model):
    STATUS_CHOICES = (
        ('ship', 'Доставка'),
        ('return', 'Возврат'),
        ('payment', 'Оплата'),
        ('about', 'О нас'),
        ('contacts', 'Контакты'),
    )

    header = models.CharField('Заголовок', max_length=100, null=True, blank=True)
    text = models.TextField('Текст')
    status = models.CharField('Раздел сайта', choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Текст'

    def __str__(self):
        return self.status.title()
