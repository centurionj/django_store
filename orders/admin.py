from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'status', 'date_created')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('date_created',)
    inlines = [OrderItemInline]
