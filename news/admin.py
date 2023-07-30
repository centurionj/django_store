from django.contrib import admin

from .models import News
from aut.models import UserProfile
from .tasks import send_spam_task


def spam(modeladmin, request, queryset):
    """
    рассылка новостей
    """

    recipient_list = list(UserProfile.objects.filter(ready_to_spam=True).values_list('user__email', flat=True))
    news = queryset.first()
    subject = news.title
    message = news.content

    # Вызываем задачу Celery для отправки спама
    send_spam_task.delay(subject, message, recipient_list)


spam.short_description = "SPAM"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    search_fields = ('title',)
    readonly_fields = ('date_created',)
    actions = [spam]
