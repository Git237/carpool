from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django import forms
from datetime import datetime, timezone
# Create your models here.
class Driver(models.Model):
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, null=True)
    email = models.EmailField(max_length=200, null=True)
    avatar = models.ImageField(default='avatar.png', upload_to='pics/')

    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}--{self.date_created.strftime('%d-%m-%Y')}"

STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

class Relationship(models.Model):
    sender = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}--{self.receiver}"


class coffee(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    

class feedbackmodel(models.Model):
    STATUS_CHOICES = (
    ('yes', 'yes'),
    ('no', 'no'),
)

    STATUS_CHOICES2 = (
    ('very good', 'very good'),
    ('good', 'good'),
    ('fair', 'fair'),
    ('poor', 'poor'),
    ('very poor', 'very poor'),
)


    STATUS_CHOICES3 = (
    ('very good', 'very good'),
    ('good', 'good'),
    ('fair', 'fair'),
    ('poor', 'poor'),
    ('very poor', 'very poor'),
)

    STATUS_CHOICES4 = (
    ('very good', 'very good'),
    ('good', 'good'),
    ('fair', 'fair'),
    ('poor', 'poor'),
    ('very poor', 'very poor'),
)

    STATUS_CHOICES5 = (
    ('very good', 'very good'),
    ('good', 'good'),
    ('fair', 'fair'),
    ('poor', 'poor'),
    ('very poor', 'very poor'),
)

    STATUS_CHOICES6 = (
    ('yes', 'yes'),
    ('no', 'no'),
)

    clean_car = models.CharField(max_length=8, choices=STATUS_CHOICES)
    condition_of_seats = models.CharField(max_length=10, choices=STATUS_CHOICES2)
    Behaviour_of_Driver= models.CharField(max_length=10, choices=STATUS_CHOICES3)
    Driving_Skills = models.CharField(max_length=10, choices=STATUS_CHOICES4)
    Level_of_comfort = models.CharField(max_length=10, choices=STATUS_CHOICES5)
    recommend = models.CharField(max_length=8, choices=STATUS_CHOICES6)

    def __str__(self):
        return self.clean_car
