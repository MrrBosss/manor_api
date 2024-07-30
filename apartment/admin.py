from django.contrib import admin

from .models import Apartment, ApartmentShots, Order, OrderItem
# Register your models here.

admin.site.register(Apartment)

admin.site.register(ApartmentShots)

admin.site.register(Order)

admin.site.register(OrderItem)

