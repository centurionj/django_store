from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок',max_length=255)
    content = models.TextField('Текст письма',)
    date_created = models.DateTimeField('Дата',auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Рассылка'
        verbose_name = 'Рассылки'
        ordering = ['date_created']

    def __str__(self):
        return self.title