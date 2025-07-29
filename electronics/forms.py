from django import forms
from .models import Product

# NEW: Import Django's built-in UserCreationForm and User model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# This is your existing form for products
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "image"]

# NEW: This form handles new user registration
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')