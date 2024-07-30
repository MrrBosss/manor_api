from rest_framework import serializers

from .models import Apartment, ApartmentShots, Order, OrderItem


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


class ApartmentShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentShots
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