from django.urls import path
from product.apps import ProductConfig
from product.views import categories, ProductListView, ProductDetailView, category_product, index

app_name = ProductConfig.name


urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/product/', category_product, name='category_product'),
]