# Generated by Django 4.2.2 on 2023-08-14 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0002_alter_logo_options_remove_logo_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(upload_to='', verbose_name='Фото'),
        ),
    ]
