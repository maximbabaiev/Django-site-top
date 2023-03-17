from django.contrib import admin
from products.models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    extra = 0
    readonly_fields = ('created_timestamp',)
