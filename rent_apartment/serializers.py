from  rest_framework import serializers 
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import RentApartment, RentApartmentShots, RentApartmentOrder, RentApartmentOrderItem, Location, Convenience,\
                    Condition, Characteristic, ApartmentCharacteristic
from apartment.serializers import CategorySerializer, BrandSerializer, CitySerializer,\
                                    DistrictSerializer


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'


class RentApartmentShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentApartmentShots
        fields = '__all__'


class ConvenienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenience
        fields = '__all__'


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
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


class RentApartmenCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentCharacteristic
        fields = '__all__'


class RentApartmentDetailSerializer(serializers.ModelSerializer):
    rent_shots = RentApartmentShotsSerializer(many=True)
    brand = BrandSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    characteristics = RentApartmenCharacteristicSerializer(read_only=True,many=True)
    locations = LocationSerializer(read_only=True,many=True)
    convenience = ConvenienceSerializer(read_only=True)
    condition = ConditionSerializer(read_only=True)
    
    class Meta: 
        model = RentApartment
        fields = '__all__'


class RentApartmentSerializer(serializers.ModelSerializer):
    rent_shots = RentApartmentShotsSerializer(many=True)
    brand = BrandSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    characteristics = RentApartmenCharacteristicSerializer(read_only=True,many=True)
    convenience = ConvenienceSerializer(read_only=True)
    condition = ConditionSerializer(read_only=True)
    locations = LocationSerializer(read_only=True,many=True)
    
    class Meta:
        model = RentApartment
        fields = '__all__'


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
