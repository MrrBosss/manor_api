from django.contrib import admin

from .models import Apartment, ApartmentShots, Order, OrderItem
# Register your models here.


class ApartmentShotsInline(admin.TabularInline):
    model = ApartmentShots
    extra = 0

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['name','company_logo','company_name','id']
    search_fields = ['name']
    list_display_links = ['name','company_logo']
    inlines = [ApartmentShotsInline]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'id']
    list_display_links =  ['order_date','id']
    inlines = [OrderItemInline]

    def get_total_quantity(self, obj):
        return sum(item.quantity for item in obj.items.all())

    get_total_quantity.short_description = 'Total Quantity'

