import django.contrib.auth.models as modelss
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import *
from .models import *


class Login(forms.Form):
    username = forms.CharField(min_length=4, label='Логин',required=True)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Пароль')


class RegisterForm(forms.Form):
    username = CharField(required=True, min_length=4, label='Логин')
    password1 = CharField(required=True, min_length=8, widget=widgets.PasswordInput, label='Пароль')
    password2 = CharField(required=True, min_length=8, widget=widgets.PasswordInput, label='Подтверждение пароля')


class UserCreateForm(UserCreationForm):
    # email = EmailField(required=True, widget=widgets.TextInput(attrs={'placeholder': 'Email', 'type': 'email'}))
    first_name = CharField(required=True, widget=widgets.TextInput(attrs={'placeholder': 'Имя'}))
    # last_name = CharField(required=True, widget=widgets.TextInput(attrs={'placeholder': 'Фамилия'}))
    username = CharField(required=True, widget=widgets.TextInput(attrs={'placeholder': 'Логин'}))
    password1 = CharField(required=True, widget=widgets.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = CharField(required=True, widget=widgets.PasswordInput(attrs={'placeholder': 'Подтверждение пароля'}))

    class Meta:
        fields = [
            # 'email',
            'first_name',
            # 'last_name',
            'username',
            'password1',
            'password2'
        ]
        model = User


class RegistrationForm(UserCreationForm):
    username = CharField(min_length=5, label='Логин')
    password1 = CharField(min_length=8, widget=PasswordInput, label='Пароль')
    password2 = CharField(min_length=8, widget=PasswordInput, label='Повторите ввод')
    email = EmailField(label='Email')
    first_name = CharField(max_length=30, label='Введите имя')
    last_name = CharField(max_length=30, label='Введите фамилию')

    class Meta:
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name'
        ]
        model = modelss.User
