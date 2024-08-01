from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Apartment, ApartmentShots, Order, OrderItem, Brand, City, District
# Register your models here.

class ApartmentShotsInline(admin.TabularInline):
    model = ApartmentShots
    extra = 0

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['name','brand','city','district','id']
    search_fields = ['company_name', 'name']
    list_display_links = ['name','brand']
    inlines = [ApartmentShotsInline]

    def get_logo(self, obj):
        image = obj.image.url if obj.image else ""
        return mark_safe(
            f'<img src="{image}" width="200"/>'  # if obj.logo_light else '<div>Rasmsiz</div>'
        )

    get_logo.short_description = 'Логотип'
    get_logo.allow_tags = True


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'id']
    list_display_links =  ['order_date','id']
    inlines = [OrderItemInline]

    # def get_total_quantity(self, obj):
    #     return sum(item.quantity for item in obj.items.all())

    # get_total_quantity.short_description = 'Total Quantity'

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    list_display_links = ['name']
    search_fields = ['name']

class DistrictInline(admin.TabularInline):
    model = District
    extra = 0

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    list_display_links = ['name']
    search_fields = ['name','district']
    inlines = [DistrictInline]


