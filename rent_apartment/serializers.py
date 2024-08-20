from  rest_framework import serializers 
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import RentApartment, RentApartmentShots, RentApartmentOrder, RentApartmentOrderItem, Location


class RentApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentApartment
        fields = '__all__'


class RentApartmentShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentApartmentShots
        fields = '__all__'

   
class LocationSerializer(serializers.ModelSerializer):
    # latitude = serializers.SerializerMethodField()
    # longitude = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ['id', 'name', 'location']
        geo_field = 'location'  # Specify the geographical field

    def get_latitude(self, obj) -> float:
        if hasattr(obj, 'location') and obj.location:
            return obj.location.y
        



    def get_longitude(self, obj) -> float:
        if hasattr(obj, 'location') and obj.location:
            return obj.location.x
        return None

class RentApartmentOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentApartmentOrderItem
        fields = ['id', 'apartment']


class RentApartmentOrderSerializer(serializers.ModelSerializer):
    items = RentApartmentOrderItemSerializer(many=True)

    class Meta:
        model = RentApartmentOrder
        fields = ['id', 'order_date', 'name', 'phone_number', 'comment', 'items']

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Items list cannot be empty")
        return value

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = RentApartmentOrder.objects.create(**validated_data)
        for item_data in items_data:
            RentApartmentOrderItem.objects.create(order=order, **item_data)
        return order