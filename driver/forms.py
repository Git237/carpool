from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import *
from django import forms
from django.contrib.auth.models import User



class CustomUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']






