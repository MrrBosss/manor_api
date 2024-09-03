from django.contrib import admin
from modeltranslation.admin import  TranslationAdmin
from django.utils.safestring import mark_safe


from .models import Apartment, ApartmentShots, Order, OrderItem, Brand, City, District, Category,\
                    Project, Features
from .forms import ApartmentForm
from rent_apartment.models import ApartmentCharacteristic
# Register your models here.

class ProjectInline(admin.TabularInline):
    model =  Project
    extra = 0
    fieldsets = (
        ('Project Information', {
            'fields': ('brand', 'name')
        }),
    )

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    list_display_links = ['name']
    search_fields = ['name']
    inlines = [ProjectInline]
    fieldsets = (
        ('Brand', {
            'fields': ('name', 'apartment_sold','year_join','brand_image')
        }),
    )

class DistrictInline(admin.TabularInline):
    model = District
    extra = 0
    fieldsets = (
        ('Tuman', {
            'fields': ('name', 'city')
        }),
    )

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    list_display_links = ['name']
    search_fields = ['name','district']
    inlines = [DistrictInline]
    fieldsets = (
        ('Shahar ', {
            'fields': ('name',)
        }),
    )

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name_uz','id']
    list_display_links = ['name_uz']
    search_fields = ['name']
    

class ApartmentCharacteristicInline(admin.TabularInline):
    model = ApartmentCharacteristic
    extra = 0
    fieldsets = (
        ("Xarakteristika", {
            'fields': ('apartment','characteristic','value')
        }),
    )

class ApartmentShotsInline(admin.TabularInline):
    model = ApartmentShots
    extra = 0
    fieldsets = (
        ('Turar joy rasmlari', {
            'fields': ('apartment', 'image')
        }),
    )

@admin.register(Apartment)
class ApartmentAdmin(TranslationAdmin):
    list_display = ['name_uz','brand','room','project','city','district','id']
    search_fields = ['company_name', 'name','room']
    list_display_links = ['name_uz','brand','room']
    inlines = [ApartmentShotsInline,ApartmentCharacteristicInline]
    form = ApartmentForm

    # Define fieldsets to group and order fields in the form view
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
        ('Umumiy malumot', {
            'fields': ('room','brand','project','category','city', 'district', 'mortgage_available')
        }),
        ('Narx va Boshqalar', {
            'fields': ('price', 'price_per_m','feature')
        }),
    )

    def get_logo(self, obj):
        image = obj.image.url if obj.image else ""
        return mark_safe(
            f'<img src="{image}" width="200"/>'  # if obj.logo_light else '<div>Rasmsiz</div>'
        )

    get_logo.short_description = 'Логотип'
    get_logo.allow_tags = True


@admin.register(Features)
class FeaturesAdmin(TranslationAdmin):
    list_display = ['text_uz','id']
    list_display_links = ['text_uz','id']
    

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'id']
    list_display_links =  ['order_date','id']
    inlines = [OrderItemInline]
   
