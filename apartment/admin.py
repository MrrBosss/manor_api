from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline
from django_admin_geomap import ModelAdmin
from django.utils.safestring import mark_safe

from .models import Apartment, ApartmentShots, Order, OrderItem, Brand, City, District, Category, Location
# Register your models here.

class Admin(ModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_autozoom = "10"
    geomap_item_zoom = "10"
    geomap_new_feature_icon = "/myicon.png"
    geomap_default_longitude = "95.1849"
    geomap_default_latitude = "64.2637"
    geomap_default_zoom = "3"
    geomap_height = "300px"
    # geomap_show_map_on_list = True

class ApartmentShotsInline(admin.TabularInline):
    model = ApartmentShots
    extra = 0

class ApartmentLocationInline(admin.TabularInline):
    model = Location
    extra = 1
    
@admin.register(Apartment)
class ApartmentAdmin(TabbedTranslationAdmin):
    list_display = ['name_uz','brand','city','district','id']
    search_fields = ['company_name', 'name']
    list_display_links = ['name_uz','brand']
    inlines = [ApartmentShotsInline,ApartmentLocationInline]

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

@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ['name_uz','id']
    list_display_links = ['name_uz']
    search_fields = ['name']
