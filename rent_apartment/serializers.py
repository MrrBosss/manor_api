from  rest_framework import serializers 

from .models import RentApartment, RentApartmentShots, RentApartmentOrder, RentApartmentOrderItem


class RentApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentApartment
        fields = '__all__'


class RentApartmentShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentApartmentShots
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