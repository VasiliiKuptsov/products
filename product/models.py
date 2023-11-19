from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


from datetime import datetime
# Create your models here.
NULLABLE = {'blank': True, 'null': True}

class Category (models.Model):

    name = models.CharField(max_length = 200, verbose_name= 'наименование категории')
    description = models.TextField(**NULLABLE, verbose_name='описание категории')
    #created_at = models.IntegerField(**NULLABLE)


    def __str__(self):
        return  f'{self.name}'


    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product (models.Model):

    name = models.CharField(max_length=200, verbose_name='наименование')
    slug = models.CharField(max_length=100, **NULLABLE, verbose_name='Slug')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(upload_to = 'catalog/', **NULLABLE, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    purchase_price = models.IntegerField(**NULLABLE, verbose_name='цена за покупку')
    publication = models.BooleanField(default=True, verbose_name='Опубликовано')
    date_of_creation = models.DateField(**NULLABLE, verbose_name='дата создания')
    date_of_last_modification = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')

    def __str__(self):
        return  f'{self.name}({self.category}){self.purchase_price}'


    class Meta:

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'



class Version(models.Model):
    VERSION_CHOICES = ((True, 'активная'), (False, 'не активная'))

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(default=1, blank=True, verbose_name='Номер версии')
    version_name = models.CharField(max_length=250, verbose_name='Название версии')
    is_current = models.BooleanField(choices=VERSION_CHOICES, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.product} {self.version_number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('version_number',)


@receiver(post_save, sender=Version)
def set_current_version(sender, instance, **kwargs):
    if instance.is_current:
        Version.objects.filter(product=instance.product).exclude(pk=instance.pk).update(is_current=False)

