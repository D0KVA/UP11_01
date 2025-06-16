from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'description', 'price', 'photo', 'is_exists', 'category', 'collection', 'brand', 'supplier']

class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info', 'photo']

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class CollectionsForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'description']

class BrandsForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'country']

class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        min_length=2
    )
    email = forms.EmailField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Придумайте пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        min_length=2
    )
    password = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    