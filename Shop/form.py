from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your userName'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your EmailId'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your Conform Password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
