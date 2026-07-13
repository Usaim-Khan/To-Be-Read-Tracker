from django.contrib.auth.forms import UserCreationForm # signup
from django.contrib.auth.models import User # signup
from django import forms # login


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'********'}))

    
    

