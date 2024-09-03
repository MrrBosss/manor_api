from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationAdmin
from django.contrib.gis.db import models
import mapwidgets


from .models import RentApartment, RentApartmentShots, RentApartmentOrder, RentApartmentOrderItem, Location, Convenience,\
                    Condition, Characteristic, ApartmentCharacteristic
# Register your models here.

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name','apartment','rent_apartment','id']
    list_display_links = ['name','apartment','rent_apartment','id']
    search_fields = ['name','id']
    formfield_overrides = {
        models.PointField: {"widget": mapwidgets.LeafletPointFieldWidget}
    }


@admin.register(Convenience)
class ConvenienceAdmin(TranslationAdmin):
    list_display = ('name','id')
    list_display_links = ('name','id')
    search_fields = ('name',)


@admin.register(Condition)
class ConditionAdmin(TranslationAdmin):
    list_display = ('name','id')
    list_display_links = ('name','id')
    search_fields = ('name',)


@admin.register(Characteristic)
class CharacteristicAdmin(TranslationAdmin):
    list_display = ('id','label')
    list_display_links = ('id','label')
    search_fields = ('label',)


class ApartmentCharacteristicInline(admin.TabularInline):
    model = ApartmentCharacteristic
    extra = 0

class RentApartmentShotsInline(admin.TabularInline):
    model = RentApartmentShots
    extra = 0

@admin.register(RentApartment)
class RentApartmentAdmin(TranslationAdmin):
    list_display = ['name_uz','tenant_name','brand','id']
    search_fields = ['name']
    list_display_links = ['name_uz','tenant_name']
    inlines = [RentApartmentShotsInline,ApartmentCharacteristicInline]
    fieldsets = (
        ('Uzbek (Default)', {
            'classes': ('collapse',),  # You can remove 'collapse' if you don't want it collapsed
            'fields': ('name_uz', 'description_uz')
        }),
        ('English', {
            'classes': ('collapse',),  # You can remove 'collapse' if you don't want it collapsed
            'fields': ('name_en', 'description_en')
        }),
        ('Russian', {
            'classes': ('collapse',),  # You can remove 'collapse' if you don't want it collapsed
            'fields': ('name_ru', 'description_ru',)
        }),
        ("Ijara beruvchi ma'lumotlari", {
            'fields': ('tenant_name', 'tenant_image', 'apartment_sold')
        }),
        ("Narx va boshqalar", {
            'fields': ('price_per_m','characteristic','convenience', 'condition')
        }),
        ("Manzil va boshqalar", {
            'fields': ('brand', 'city', 'district', 'category')
        }),
    )


class OrderItemInline(admin.TabularInline):
    model = RentApartmentOrderItem
    extra = 0

@admin.register(RentApartmentOrder)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'id']
    list_display_links =  ['order_date','id']
    inlines = [OrderItemInline]

    # def get_total_quantity(self, obj):
    #     return sum(item.quantity for item in obj.items.all())

    # get_total_quantity.short_description = 'Total Quantity'
