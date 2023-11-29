from django.db import models
from product.models import NULLABLE
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=20, verbose_name='страна', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='активный')
    key = models.CharField(max_length=25, unique=True, verbose_name='ключ пользователя', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True


class EmailVerificationToken(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь')

    token = models.CharField(max_length=255, unique=True, verbose_name='токен верификации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания токена')

    def __str__(self):
        return f'{self.token} {self.created_at}'

