from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline
from django.utils.safestring import mark_safe

from .models import Apartment, ApartmentShots, Order, OrderItem, Brand, City, District, Category, Characteristic
# Register your models here.

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


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ['name_uz','id']
    list_display_links = ['name_uz']
    search_fields = ['name']


class ApartmentShotsInline(admin.TabularInline):
    model = ApartmentShots
    extra = 0
    
@admin.register(Apartment)
class ApartmentAdmin(TabbedTranslationAdmin):
    list_display = ['name_uz','brand','city','district','id']
    search_fields = ['company_name', 'name']
    list_display_links = ['name_uz','brand']
    inlines = [ApartmentShotsInline]

    def get_logo(self, obj):
        image = obj.image.url if obj.image else ""
        return mark_safe(
            f'<img src="{image}" width="200"/>'  # if obj.logo_light else '<div>Rasmsiz</div>'
        )

    get_logo.short_description = 'Логотип'
    get_logo.allow_tags = True

@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['id','type']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'id']
    list_display_links =  ['order_date','id']
    inlines = [OrderItemInline]

