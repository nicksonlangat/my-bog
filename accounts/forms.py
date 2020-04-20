from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegistratonForm(UserCreationForm):
    email       =   forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={
        'placeholder':'yourname@example.com' 
    }))
    password1  =   forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password'
    }))

    class Meta:
        model   =   User
        fields  =   ['username','email', 'password1', 'password2']


class UpdateProfile(forms.ModelForm):
    email       =   forms.EmailField(max_length=100, required=False)

    class Meta:
        model   =   User
        fields  =   [ 'email']

