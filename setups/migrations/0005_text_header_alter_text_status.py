# Generated by Django 4.2.2 on 2023-08-15 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0004_alter_photo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='header',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='text',
            name='status',
            field=models.CharField(choices=[('ship', 'Доставка'), ('return', 'Возврат'), ('payment', 'Оплата'), ('about', 'О нас'), ('contacts', 'Контакты')], verbose_name='Раздел сайта'),
        ),
    ]
