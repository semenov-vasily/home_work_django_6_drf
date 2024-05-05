from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60, unique=True, verbose_name="Название продукта")
    description = models.TextField(null=True, blank=True, verbose_name="Описание продукта")

    class Meta:
        ordering = ['id']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Stock(models.Model):
    address = models.CharField(max_length=200, unique=True, verbose_name="Адрес склада")
    products = models.ManyToManyField(Product, through='StockProduct', related_name='stocks', verbose_name="Продукт")

    class Meta:
        ordering = ['id']
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.address


class StockProduct(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='positions', verbose_name="Адрес склада")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='positions', verbose_name="Продукт")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество продуктов")
    price = models.DecimalField(max_digits=18, decimal_places=2, validators=[MinValueValidator(0)],
                                verbose_name="Цена продукта")

    class Meta:
        ordering = ['id']
        verbose_name = 'Продукты на складе'
        verbose_name_plural = 'Продукты на складе'

    def __str__(self):
        return f'{self.stock} {self.product}'