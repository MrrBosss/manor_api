from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import Banner, News, Advertisement
from .serializers import NewsSerializer, BannerSerizlizer,AdvertisementSerializer
# Create your views here.


class AdvertisementView(generics.CreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    http_method_names = ['post']
    pagination_class = None


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerizlizer
    http_method_names = ['get']
    pagination_class = None


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    http_method_names = ['get']
    pagination_class = None