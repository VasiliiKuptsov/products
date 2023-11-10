from django.db import models
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
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(upload_to = 'catalog/', **NULLABLE, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    purchase_price = models.IntegerField(**NULLABLE, verbose_name='цена за покупку')
    date_of_creation = models.DateField(**NULLABLE, verbose_name='дата создания')
    date_of_last_modification = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')

    def __str__(self):
        return  f'{self.name}({self.category}){self.purchase_price}'


    class Meta:

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

# Create your models here.
