import django.contrib.auth.models as authmodel
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import *
from .models import *


class Login(forms.Form):
    username = forms.CharField(min_length=4, label='Логин',required=True)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Пароль')


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Login')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Repeat Password')
    # email = forms.EmailField(label='Email')
    # first_name = forms.CharField(label='First name')
    # last_name = forms.CharField(label='Last name')
