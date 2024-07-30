from django.shortcuts import render
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Apartment, ApartmentShots, Order
from .serializers import ApartmentSerializer, ApartmentShotsSerializers, OrderSerializer
# Create your views here.


class ApartmentListView(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    search_fields = ['name']


class ApartmentDetailView(generics.RetrieveAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class ApartmentShotsViewSet(viewsets.ModelViewSet):
    queryset = ApartmentShots.objects.all()
    serializer_class = ApartmentShotsSerializers
    http_method_names = ['get']
    pagination_class = None


class OrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['post']
    pagination_class = None
