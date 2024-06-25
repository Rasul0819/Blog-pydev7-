from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from . import models
class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name','password1','password2']
    
class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields = ['username','password']

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ('title', 'description', 'image','updated','author')