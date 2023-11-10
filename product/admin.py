
from django.contrib import admin
from product.models import Product, Category
#

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_filter = ('category',)
# Register your models here.
