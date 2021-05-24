from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import datetime, timezone


# Create your models here.


class Carformmodel(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    start_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    start_time = models.CharField(null=True,max_length=255)
    journey_time = models.CharField(null=True,max_length=255)
    fare = models.IntegerField(null=True)
    date = models.DateField(null=True)
    capacity = models.IntegerField(null=True)
    contact_Number = models.IntegerField(null=True,max_length=10)
    vehicle_Number = models.CharField(null=True,max_length=10)
    license = models.ImageField(null=True,blank=True)
    

    def __str__(self):
        return self.start_location


class Bikeformmodel(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    start_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    start_time = models.CharField(null=True,max_length=255)
    journey_time = models.CharField(null=True,max_length=255)
    fare = models.IntegerField(null=True)
    date =  models.DateField(null=True)
    capacity = models.IntegerField(default='1',editable=False)
    contact_Number = models.IntegerField(null=True,max_length=10)
    vehicle_Number = models.CharField(null=True,max_length=10)
    license = models.ImageField(null=True,blank=True)
    

    def __str__(self):
        return self.start_location

class TruckformModel(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    start_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    start_time = models.CharField(null=True,max_length=255)
    date =  models.DateField(null=True)
    no_of_cartoon = models.IntegerField(null=True)
    contact_Number = models.IntegerField(null=True,max_length=10)
    license = models.ImageField(null=True, blank=True)

    
    def __str__(self):
        return self.start_location