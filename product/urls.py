from django.urls import path
from product.apps import ProductConfig
from product.views import CategoryListView, ProductListView, ProductCreateView, ContactsPageView, ProductDetailView, ProductUpdateView, ProductDeleteView

app_name = ProductConfig.name


urlpatterns = [
    #path('', index, name='index'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('', ProductListView.as_view(), name='index'),
    #path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    #path('categories/', CategoryListView.as_view(), name='categories'),#categories
    #path('product/<int:pk>/', ProductListView.as_view(), name='category_product'),#category_product
    #path('product/create/', ProductCreateView.as_view(), name='product_create'),
]