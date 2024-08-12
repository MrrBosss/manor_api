from rest_framework import serializers 

from .models import News, Banner


class BannerSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
