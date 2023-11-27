from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms
from product.forms import StyleFormMixin
class UserRegisterForm(UserCreationForm, StyleFormMixin):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'password', 'phone', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()



