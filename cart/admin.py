from django.contrib import admin

from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active')
    search_fields = ('user__username', 'user__email')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'size', 'quantity', 'price', 'is_promo_used')
    list_filter = ('cart',)
    search_fields = ('cart__user__username', 'cart__user__email', 'product__name')
