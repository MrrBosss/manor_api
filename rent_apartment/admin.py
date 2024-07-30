from django.contrib import admin

from .models import RentApartment, RentApartmentShots, RentApartmentOrder, RentApartmentOrderItem
# Register your models here.

admin.site.register(RentApartment)

admin.site.register(RentApartmentShots)

class OrderItemInline(admin.TabularInline):
    model = RentApartmentOrderItem
    extra = 0


@admin.register(RentApartmentOrder)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'id']
    list_display_links =  ['order_date','id']
    inlines = [OrderItemInline]

    def get_total_quantity(self, obj):
        return sum(item.quantity for item in obj.items.all())

    get_total_quantity.short_description = 'Total Quantity'
