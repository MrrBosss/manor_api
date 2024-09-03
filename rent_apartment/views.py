from django.shortcuts import render
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend


from .models import RentApartment, RentApartmentShots, RentApartmentOrder, Location, Convenience, Condition, Characteristic
from .serializers import RentApartmentSerializer, RentApartmentShotsSerializer, RentApartmentOrderSerializer,\
                        LocationSerializer,ConvenienceSerializer, ConditionSerializer, RentApartmentDetailSerializer,\
                        CharacteristicSerializer
from .filters import RentApartmentFilter
# Create your views here.


class CharacteristicViewSet(viewsets.ModelViewSet):
    queryset = Characteristic
    serializer_class = CharacteristicSerializer
    pagination_class = None
    


class RentApartmentListView(generics.ListAPIView):
    queryset = RentApartment.objects.all()
    serializer_class = RentApartmentSerializer
    search_fields = ['name']
    filter_backends = [DjangoFilterBackend]
    filterset_class = RentApartmentFilter

class RentApartmentDetailView(generics.RetrieveAPIView):
    queryset = RentApartment.objects.all()
    serializer_class = RentApartmentDetailSerializer


class RentApartmentShotsViewSet(viewsets.ModelViewSet):
    queryset = RentApartmentShots.objects.all()
    serializer_class = RentApartmentShotsSerializer
    http_method_names = ['get']
    pagination_class = None


class ConvenienceViewSet(viewsets.ModelViewSet):
    queryset = Convenience.objects.all()
    serializer_class = ConvenienceSerializer
    http_method_names = ['get']
    pagination_class = None


class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    http_method_names = ['get']
    pagination_class = None

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    http_method_names = ['get']
    pagination_class = None

class RentOrderView(generics.CreateAPIView):
    queryset = RentApartmentOrder.objects.all()
    serializer_class = RentApartmentOrderSerializer
    http_method_names = ['post']



    