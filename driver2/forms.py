from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from .models import Carformmodel, Bikeformmodel, TruckformModel


class RegdriverForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This mail address is already in use')
        username = self.cleaned_data.get('email')
        try:
            match = User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise forms.ValidationError('This username is already in use')


    def save(self, commit=True):
        user = super(RegdriverForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user 

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class CarformmodelForm(ModelForm):
    class Meta:
        model = Carformmodel
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'start_time': TimeInput(format='%H:%M'),
            'journey_time': TimeInput(format='%H:%M'),
        }

class BikeformmodelForm(ModelForm):
    class Meta:
        model = Bikeformmodel
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'start_time': TimeInput(format='%H:%M'),
            'journey_time': TimeInput(format='%H:%M'),
        }

class TruckformmodelForm(ModelForm):
    class Meta:
        model = TruckformModel
        fields = '__all__'