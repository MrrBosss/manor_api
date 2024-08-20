from django.shortcuts import render
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend


from .models import RentApartment, RentApartmentShots, RentApartmentOrder, Location
from .serializers import RentApartmentSerializer, RentApartmentShotsSerializer, RentApartmentOrderSerializer,\
                        LocationSerializer
from .filters import RentApartmentFilter
# Create your views here.


class RentApartmentListView(generics.ListAPIView):
    queryset = RentApartment.objects.all()
    serializer_class = RentApartmentSerializer
    search_fields = ['name']
    filter_backends = [DjangoFilterBackend]
    filterset_class = RentApartmentFilter

class RentApartmentDetailView(generics.RetrieveAPIView):
    queryset = RentApartment.objects.all()
    serializer_class = RentApartmentSerializer


class RentApartmentShotsViewSet(viewsets.ModelViewSet):
    queryset = RentApartmentShots.objects.all()
    serializer_class = RentApartmentShotsSerializer
    http_method_names = ['get']
    pagination_class = None


class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class RentOrderView(generics.CreateAPIView):
    queryset = RentApartmentOrder.objects.all()
    serializer_class = RentApartmentOrderSerializer
    http_method_names = ['post']



    