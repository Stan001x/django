from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class":"fw-bolder", 'placeholder':'mail@mail.com'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"fw-bolder", 'placeholder':'Семен'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"fw-bolder", 'placeholder':'***'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"fw-bolder", 'placeholder':'***'}))

    class Meta:
        model=User
        fields = ("username", "email", "password1", "password2")

