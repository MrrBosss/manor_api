from rest_framework import serializers 

from .models import News, Banner, Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'order_date', 'name', 'phone_number', 'comment',]


class BannerSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
