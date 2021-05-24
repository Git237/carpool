from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import  RegdriverForm, CarformmodelForm, BikeformmodelForm, TruckformmodelForm
from django.contrib import messages
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from .models import*
from .decorators import allowed_users
# Create your views here.

def regdriver(request):
    form = RegdriverForm()
    if request.method == 'POST':
        form = RegdriverForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' +  user)
            return redirect('login2')

    context = {'form':form}
    return render(request, 'driver2/registerasdriver.html', context)


def login2(request):
   
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('ddashboard')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'driver2/login2.html', context)

def logout2(request):
    logout(request)
    return redirect('index')

def ddashboard(request):
    return render(request, 'driver2/ddashboard.html')

def carform(request):
    form = CarformmodelForm()
    if request.method == 'POST':
        form = CarformmodelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'driver2/carform.html',context)

def bikeform(request):
    form = BikeformmodelForm()
    if request.method == 'POST':
        form = BikeformmodelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'driver2/bikeform.html',context)

def map2(request):
    return render(request, 'driver2/map2.html')


def truckform(request):
    form = TruckformmodelForm()
    if request.method == 'POST':
        form = TruckformmodelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'driver2/truckform.html',context)
