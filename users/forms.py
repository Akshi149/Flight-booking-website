from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, ReadOnlyPasswordHashField
from .models import Profile

#For User Regestration
class user_reg_form(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model= User
        fields=['username','email','password1','password2']

#For User login   
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
