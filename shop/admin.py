from django.contrib import admin
from .models import Product, Purchase, Promocode, PromocodeProduct

# Регистрируем модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Выводим на главной странице товара название и цену
    search_fields = ('name',)  # Добавляем поиск по названию товара

# Регистрируем модель покупки
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('person', 'product', 'address', 'date')  # Выводим информацию о покупке
    search_fields = ('person', 'address')  # Добавляем поиск по имени и адресу

# Регистрируем модель промокода
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'date')  # Выводим код и дату создания
    search_fields = ('code',)  # Добавляем поиск по коду промокода

# Регистрируем модель связи между промокодами и товарами
class PromocodeProductAdmin(admin.ModelAdmin):
    list_display = ('promocode', 'product')  # Выводим код промокода и товар
    search_fields = ('promocode__code', 'product__name')  # Добавляем поиск по коду промокода и названию товара

# Регистрируем все модели в админке
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Promocode, PromocodeAdmin)
admin.site.register(PromocodeProduct, PromocodeProductAdmin)
