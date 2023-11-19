
from django.contrib import admin
from product.models import Product, Category, Version
#

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_price', 'category')# 'id', 'product', 'version_number', 'version_name', 'is_current',)
    list_filter = ('category',) #category
    search_fields = ('name', 'description')


@ admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
        list_display = ('id', 'product', 'version_number', 'version_name', 'is_current')
        list_filter = ('version_number',)
        search_fields = ('version_number', 'version_name',)

# Register your models here.
