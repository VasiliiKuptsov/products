
from django.shortcuts import render, get_object_or_404
from product.models import Product, Category
from django.views.generic import ListView, DetailView
# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def index(request):  #index
    context = {
        'object_list': Category.objects.all(),
        'title': 'ПРОДУКТЫ - КАТЕГОРИИ'
    }
    return render(request, 'product/index.html', context)

def categories(request):

    context = {
        'object_list': Category.objects.all(),
        'title': 'ВСЕ КАТЕГОРИИ'
    }
    return render(request, 'product/categories.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product.html'


def category_product(request, pk):
    category_item = Category.objects.get(pk=pk)

    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'ВСЕ ПРОДУКТЫ КАТЕГОРИИ: {category_item.name}'
    }
    return render(request, 'product/product.html', context)  # i i
# Create your views here.
