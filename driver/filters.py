import django_filters

from .models import *
from driver2.models import Carformmodel, Bikeformmodel,  TruckformModel
from driver2.forms import CarformmodelForm, BikeformmodelForm, TruckformmodelForm

class Carformfilter(django_filters.FilterSet):
    class Meta:
        model = Carformmodel
        fields = ['start_location', 'destination', 'date']


class Bikeformfilter(django_filters.FilterSet):
    class Meta:
        model = Bikeformmodel
        fields = ['start_location', 'destination', 'date']

class Truckformfilter(django_filters.FilterSet):
    class Meta:
        model = TruckformModel
        fields = ['start_location', 'destination', 'date']
