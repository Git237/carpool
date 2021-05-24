from django.urls import path
from . import views



urlpatterns = [
    path('login2/', views.login2, name="login2"),
    path('logout2/', views.logout2, name="logout2"),
    path('regdriver/', views.regdriver, name="registerasdriver"),
    path('ddashboard/', views.ddashboard, name="ddashboard"),
    path('carform/', views.carform, name="carform"),
    path('bikeform/', views.bikeform, name="bikeform"),
    path('truckform/', views.truckform, name="truckform"),
    path('map2/', views.map2, name="map2"),      
]
