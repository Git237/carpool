from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import feedbackmodel
from django import forms
from django.contrib.auth.models import User



class CustomUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class feedbackmodelform(ModelForm):
    class Meta:
        model = feedbackmodel
        fields = '__all__'



