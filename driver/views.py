from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from driver2.models import Carformmodel, Bikeformmodel,  TruckformModel
from driver2.forms import CarformmodelForm, BikeformmodelForm, TruckformmodelForm
from django.contrib.auth import authenticate, login, logout
from .models import coffee, feedbackmodel
from .forms import CustomUser, feedbackmodelform
import razorpay
from django.views.decorators.csrf import csrf_exempt
from .filters import Carformfilter, Bikeformfilter,  Truckformfilter

#return HttpResponse("this is homepage")



def index(request):
    return render(request, 'driver/index.html')


def signin(request):
    return render(request, 'driver/signin.html')

def signup(request):
   
    form = CustomUser()
    if request.method == 'POST':
        form = CustomUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' +  user)
            return redirect('login1')

    context = {'form':form}
    return render(request, 'driver/signup.html', context)

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None: 
            login(request, user)
            return redirect('passanger')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'driver/login1.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login1')


def passanger(request):
    
    return render(request, 'driver/passanger.html')

def bikerender(request):
    def get(self, request):
        form = BikeformmodelForm()

    form = BikeformmodelForm()
    bikeformmodels = Bikeformmodel.objects.all()
    myfilter2 = Bikeformfilter(request.GET, queryset=bikeformmodels)
    bikeformmodels = myfilter2.qs
    context = {'bikeformmodels':bikeformmodels, 'myfilter2':myfilter2}
    return render(request, 'driver/bikerender.html', context)

def carrender(request):
    def get(self, request):
        form = CarformmodelForm()

    form = CarformmodelForm()
    carformmodels = Carformmodel.objects.all()
    myfilter = Carformfilter(request.GET, queryset=carformmodels)
    carformmodels = myfilter.qs
    context = {'carformmodels':carformmodels, 'myfilter':myfilter}
    return render(request, 'driver/carrender.html', context)


def truckrender(request):
    def get(self, request):
        form = TruckformmodelForm()

    form = TruckformmodelForm()
    truckformmodels =  TruckformModel.objects.all()
    myfilter = Truckformfilter(request.GET, queryset=truckformmodels)
    truckformmodels = myfilter.qs
    context = {'truckformmodels': truckformmodels, 'myfilter':myfilter}
    return render(request, 'driver/truckrender.html', context)




def payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount")) * 100
        client = razorpay.Client(auth =("rzp_test_weLUcpZ0bJYMfD" , "n0x50KnsDor986yf8XaW9S8v"))
        payment = client.order.create({'amount':amount, 'currency':'INR' , 'payment_capture': '1'})
        print(payment)
        Ride = coffee(name = name , amount = amount , payment_id = payment['id'])
        Ride.save()
        return render(request, 'driver/payment.html', {'payment': payment})

    return render(request, 'driver/payment.html')
@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        print(a)
    return render(request, 'driver/success.html')



def feedbackform(request):
    form = feedbackmodelform()
    if request.method == 'POST':
        form = feedbackmodelform(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'driver/feedbackform.html')