from rest_framework import serializers

from .models import Apartment, ApartmentShots, Order, OrderItem


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


class ApartmentShotsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ApartmentShots
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
