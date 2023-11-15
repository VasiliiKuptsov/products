from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from materials.models import Material


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body', 'image', 'publication')
    success_url = reverse_lazy('materials:materials')
    extra_context = {
        'title': 'Создать статью'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'body', 'image', 'publication')
    extra_context = {
        'title': 'Изменить статью'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('materials:view', args=[self.object.pk])


class MaterialListView(ListView):
    model = Material
    extra_context = {
        'title': 'Статья'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class MaterialDetailView(DetailView):
    model = Material

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        post.views_count += 1
        post.save()
        context['title'] = post.title
        return context


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('materials:materials')
    extra_context = {
        'title': 'Удалить статью'
    }

# Create your views here.
