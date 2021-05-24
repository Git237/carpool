from django.urls import path
from .import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('login1/', views.loginPage, name="login1"),
    path('logout/', views.logoutUser, name="logout"),
    path('passanger/', views.passanger, name="passanger"),
    path('bikerender/', views.bikerender, name="bikerender"),
    path('carrender/', views.carrender, name="carrender"),
    path('truckrender/', views.truckrender, name="truckrender"),
    path('payment/', views.payment, name="payment"),
    path('success/', views.success, name="success"),
    path('feedbackform/', views.feedbackform, name="feedbackform"),
]



