from django.shortcuts import render
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend


from .models import RentApartment, RentApartmentShots, RentApartmentOrder, RentApartmentOrderItem
from .serializers import RentApartmentSerializer, RentApartmentShotsSerializer, RentApartmentOrderSerializer
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


class RentOrderView(generics.CreateAPIView):
    queryset = RentApartmentOrder.objects.all()
    serializer_class = RentApartmentOrderSerializer
    http_method_names = ['post']



    