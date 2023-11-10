# Generated by Django 4.2.6 on 2023-11-08 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='наименование категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='изображение')),
                ('purchase_price', models.IntegerField(blank=True, null=True, verbose_name='цена за покупку')),
                ('date_of_creation', models.DateField(blank=True, null=True, verbose_name='дата создания')),
                ('date_of_last_modification', models.DateField(blank=True, null=True, verbose_name='дата последнего изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
