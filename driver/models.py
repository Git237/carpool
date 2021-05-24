from django.db import models
from django.contrib.auth.models import User
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
    