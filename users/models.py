from django.db import models
from product.models import NULLABLE
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=20, verbose_name='страна', **NULLABLE)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

# Create your models here.
