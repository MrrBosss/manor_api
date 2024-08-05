from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline

from .models import RentApartment, RentApartmentShots, RentApartmentOrder, RentApartmentOrderItem
# Register your models here.

class RentApartmentShotsInline(admin.TabularInline):
    model = RentApartmentShots
    extra = 0

@admin.register(RentApartment)
class RentApartmentAdmin(TabbedTranslationAdmin):
    list_display = ['name_uz','tenant_name','brand','company','id']
    search_fields = ['name']
    list_display_links = ['name_uz','tenant_name']
    inlines = [RentApartmentShotsInline]


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
