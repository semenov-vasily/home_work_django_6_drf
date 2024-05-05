from django.contrib import admin

from logistic.models import Product, Stock, StockProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')
    list_editable = ('description',)
    ordering = ['id']
    fields = ['title', 'description']
    save_on_top = True
    list_per_page = 10

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'address',)
    list_display_links = ('id',)
    list_editable = ('address',)
    ordering = ['id']
    fields = ['address']
    save_on_top = True
    list_per_page = 10

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'stock', 'product', 'quantity', 'price',)
    list_display_links = ('id',)
    list_editable = ('stock', 'product', 'quantity', 'price')
    ordering = ['id']
    fields = ['stock', 'product', 'quantity', 'price']
    save_on_top = True
    list_per_page = 10