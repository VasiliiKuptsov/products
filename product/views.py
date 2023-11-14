
from django.shortcuts import render, get_object_or_404
from product.models import Product, Category
from django.views.generic import ListView, CreateView
# Create your views here.




def index(request):  #index
    context = {
        'object_list': Category.objects.all(),
        'title': 'ПРОДУKТЫ - ВСЕ КАТЕГОРИИ'
    }
    return render(request, 'product/index.html', context)

#def categories(request):

#    context = {
#        'object_list': Category.objects.all(),
#        'title': 'ВСЕ КАТЕГОРИИ'
#    }
#    return render(request, 'product/categories.html', context)
class CategoryListView(ListView):
    model = Category
    extra_context = {'title': 'ВСЕ КАТЕГОРИИ'}

#    def get_context_data(self, **kwargs):
 #       context = super().get_context_data(**kwargs)
  #      return context

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):

        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'ВСЕ ПРОДУКТЫ КАТЕГОРИИ: {category_item.name}'

        return context_data


#def category_product(request, pk):
#    category_item = Category.objects.get(pk=pk)
#
#    context = {
#        'object_list': Product.objects.filter(category_id=pk),
#        'title': f'ВСЕ ПРОДУКТЫ КАТЕГОРИИ: {category_item.name}'
#    }
#    return render(request, 'product/product.html', context)  # i i
# Create your views here.
class ProductCreateView(CreateView):
    model = Product