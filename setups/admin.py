from django.contrib import admin

from .models import Logo, Photo, Text

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('image',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'status')


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('header', 'text', 'status')
