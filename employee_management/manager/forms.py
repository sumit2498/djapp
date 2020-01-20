from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Manager
from django import forms


class RegisterForm(ModelForm):
  class Meta:
    model = Manager
    fields = '__all__'