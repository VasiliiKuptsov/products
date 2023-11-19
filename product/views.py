from django.forms import formset_factory, inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views import View
from django.shortcuts import render, get_object_or_404
from product.models import Product, Category, Version
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from product.forms import ProductForm, VersionForm
from pytils.translit import slugify
# Create your views here.

class ContactsPageView(View):
    def get(self, request):
        context = {'title': 'Контакты'}
        return render(request, 'product/contacts.html', context)

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"name:{name}, phone:{phone}, message:{message}")
        context = {'title': 'Контакты'}
        return render(request, 'product/contacts.html', context)


#def index(request):  #index
#    context = {
#        'object_list': Category.objects.all(),
#        'title': 'ПРОДУKТЫ - ВСЕ КАТЕГОРИИ'
#    }
#    return render(request, 'product/index.html', context)

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
    template_name = 'product/index.html'
    extra_context = {
        'title': 'Продукты'
    }
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset

    def get_context_data(self, *args, **kwargs):

        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        #category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        #context_data['category_pk'] = category_item.pk,
        #context_data['title'] = f'ВСЕ ПРОДУКТЫ КАТЕГОРИИ: {category_item.name}'
        for object in context['product_list']:
            active_version = Version.objects.filter(product=object, is_current=True).last()
            if active_version:
                object.active_version_number = active_version.version_number
            else:
                object.active_version_number = None
        return context


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
    form_class = ProductForm
    success_url = reverse_lazy('product:index')
    extra_context = {
        'title': 'Создать продукт'
    }

    def form_valid(self, form):
        new_product = form.save()
        new_product.slug = slugify(new_product.name)
        new_product.save()
        self.object = form.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        'title': 'Изменить продукт'
    }

    def get_form_class(self):
        return super().get_form_class()

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)

        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object, )
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        new_product = form.save()
        new_product.slug = slugify(new_product.name)
        new_product.save()
        self.object.save()
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product:view', args=[self.object.pk])


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['title'] = product.name
        return context


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:index')
    extra_context = {
        'title': 'Удаление продукта'
    }

