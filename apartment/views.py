from django.shortcuts import render
from django_admin_geomap import geomap_context
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Apartment, ApartmentShots, Order, Brand, City, District, Category, Location
from .serializers import ApartmentSerializer, ApartmentShotsSerializer, OrderSerializer, BrandSerializer, CitySerializer,\
                        DistrictSerializer, CategorySerializer, ApartmentDeatilSerializer
from .filters import ApartmentFilter
# Create your views here.


def home(request):
    return render(request, 'home.html', geomap_context(Location.objects.all(), auto_zoom="10"))


class ApartmentListView(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    search_fields = ['name']
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApartmentFilter


class ApartmentDetailView(generics.RetrieveAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentDeatilSerializer


class ApartmentShotsViewSet(viewsets.ModelViewSet):
    queryset = ApartmentShots.objects.all()
    serializer_class = ApartmentShotsSerializer
    http_method_names = ['get']
    pagination_class = None


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    http_method_names = ['get']
    pagination_class = None


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    http_method_names = ['get']
    

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    http_method_names = ['get']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']
    pagination_class = None


class OrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['post']
    
