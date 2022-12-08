from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserRequest


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)

    class Meta:
        model = User # создание формы из модели User
        fields = ['username', 'email', 'password1', 'password2',]


class JobApplyForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = ['job']