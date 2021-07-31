from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


    class Meta:
        model = User
        fields = ["username", "first_name","last_name","email", "password1", "password2"]

class bookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class authorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class categoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class publishForm(ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'
