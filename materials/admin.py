
from django.contrib import admin
from materials.models import Material
@admin.register(Material)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'body', 'created_at', 'publication', 'views_count')
    search_fields = ('title', 'body', 'slug')

# Register your models here.
