from django.urls import path
from product.apps import ProductConfig
from product.views import CategoryListView, ProductListView, index, ProductCreateView

app_name = ProductConfig.name


urlpatterns = [
    path('', index, name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'), #categories
    path('product/<int:pk>/', ProductListView.as_view(), name='category_product'),#category_product
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
]