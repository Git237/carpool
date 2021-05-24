from django.contrib import admin
from .models import Driver, Relationship
from django.contrib.auth.forms import UserCreationForm

# Register your models here.
admin.site.register(Driver)
admin.site.register(Relationship)


