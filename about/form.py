from django import forms
from .models import Cat, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['id', 'name', 'temperament', 'description', 'wikipedia_url', 'image']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')  # Укажите необходимые поля регистрации


class AuthForm(AuthenticationForm):
    pass
