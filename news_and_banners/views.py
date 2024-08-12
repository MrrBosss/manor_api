from django.shortcuts import render
from rest_framework import viewsets

from .models import Banner, News
from .serializers import NewsSerializer, BannerSerizlizer
# Create your views here.


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