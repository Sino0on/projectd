from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class ApplocationCreateFrom(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['employer', 'date', 'category']
        # widgets = {
        #     'employer': forms.ChoiceField()
        # }

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'