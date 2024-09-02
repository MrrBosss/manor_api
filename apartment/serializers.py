from rest_framework import serializers

from .models import Apartment, ApartmentShots, Order, OrderItem, Brand, City, District, Category, Characteristic,\
                    Project, Features



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


class CharacteristicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ['total_area', 'residential_area', 'floor', 'year_of_delivery', 'house', 'finishing', 'view_from_window', 'bathroom', 'type']


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ['text','image']


class ApartmentDeatilSerializer(serializers.ModelSerializer):
    feature = FeaturesSerializer(read_only=True)
    apartment_shots = ApartmentShotsSerializer(many=True)
    brand = BrandSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    characteristic = CharacteristicListSerializer(read_only=True)

    class Meta:
        model = Apartment
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    feature = FeaturesSerializer(read_only=True)
    apartment_shots = ApartmentShotsSerializer(many=True)
    brand = BrandSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    characteristic = CharacteristicListSerializer(read_only=True)

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
    
