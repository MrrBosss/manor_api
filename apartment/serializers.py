from rest_framework import serializers

from .models import Apartment, ApartmentShots, Order, OrderItem, Brand, City, District, Category,\
                    Project, Features
from rent_apartment.models import ApartmentCharacteristic, Location


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



class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentCharacteristic
        fields = '__all__'


class ApartmentShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentShots
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields ='__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ['id','text','image']


class ApartmentDeatilSerializer(serializers.ModelSerializer):
    features = FeaturesSerializer(read_only=True,many=True)
    apartment_shots = ApartmentShotsSerializer(many=True)
    brand = BrandSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    characteristics = CharacteristicSerializer(read_only=True,many=True)
    locations = LocationSerializer(read_only=True,many=True)

    class Meta:
        model = Apartment
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    features = FeaturesSerializer(read_only=True,many=True)
    apartment_shots = ApartmentShotsSerializer(many=True)
    brand = BrandSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    characteristics = CharacteristicSerializer(read_only=True,many=True)
    locations = LocationSerializer(read_only=True,many=True)

    class Meta:
        model = Apartment
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'apartment']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'order_date', 'name', 'phone_number','comment','items']

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Items list cannot be empty")
        return value

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
    
