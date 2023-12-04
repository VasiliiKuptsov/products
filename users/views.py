from django.http import HttpResponse
from django.shortcuts import render
import random
import string
#from django.contrib.auth.views import UserCreationform #LogoutView as BaseLogoutView
from users.models import User
from django.views.generic import CreateView
from users.forms import UserRegisterForm, UserForm

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
#class .LoginView(Bas.eLoginView):
#    template_name = 'users/user_login.html'


#class LogoutView(BaseLogoutView):
#    pass

class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/user_register.html'
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
        user = form.save(commit=False)
        user.key = token
        user.is_active = False
        user.set_password('12345')
        user.save()

        url = f"http:/127.0.0.1:8000{reverse('users:verification', args=[token])}"

        send_mail(
            subject='Регистрация',
            message=f"Для завершения регистрации перейдите по ссылке: {url} Пароль: 12345",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

        return super().form_valid(form)

    #всефвка
def verification(request, token):#verification_view
    try:

        user = User.objects.filter(key=token).first()
        user.is_active = True
        user.save()
        return redirect('users:login')
    except User.DoesNotExist:
        return HttpResponse('Неверная ссылка')
    #конец вставки
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('product:index')
    template_name = 'users/user_form.html'
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('product:index'))

class LoginView(BaseLoginView):
    template_name = 'users/user_login.html'



# Create your views here.
