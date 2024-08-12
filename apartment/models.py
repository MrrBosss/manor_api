from django.db import models
import datetime
from django_admin_geomap import GeoItem

# Create your models here.


def upload_to(instance, filename):
    # Generate filename here
    if instance.created_at:
        date_str = instance.created_at.strftime("%Y/%m/%d")
    else:
        date_str = datetime.now().strftime("%Y/%m/%d")  # Or use any default date

    return f'{date_str}/{filename}'


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.name)
    

class Brand(models.Model):
    name = models.CharField(max_length=100, null=True)
    brand_image = models.ImageField(upload_to='brand-images', blank=True)
   
    def __str__(self):
        return str(self.name)


class City(models.Model):
    name = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return str(self.name)


class District(models.Model):
    name = models.CharField(max_length=50, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)
    

class Apartment(models.Model):
    name = models.CharField(max_length=50,null=True)
    company_name = models.CharField(max_length=50,null=True)
    price = models.FloatField(default=10.000)
    price_per_m = models.FloatField(default=1.000)
    apartment_sold = models.IntegerField(default=0)
    total_area = models.FloatField(default=0)
    residential_area = models.FloatField(default=0)
    floor = models.IntegerField(default=0)
    year_of_delivery = models.IntegerField(default=0)
    house = models.CharField(max_length=100,null=True)
    finishing = models.CharField(max_length=100, null=True)
    view_from_window = models.CharField(max_length=100, null=True)
    bathroom = models.IntegerField(default=0)
    type = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    is_finish = models.BooleanField(default=False)
    mortgage_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.name)


class ApartmentShots(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE,related_name='apartment_shots',null=True)
    image = models.ImageField(upload_to=upload_to, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Shot for {self.apartment.name}"


class Location(models.Model, GeoItem):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    lon = models.FloatField()  # longitude
    lat = models.FloatField()  # latitude

    @property
    def geomap_longitude(self):
        return '' if self.lon is None else str(self.lon)

    @property
    def geomap_latitude(self):
        return '' if self.lat is None else str(self.lat)

    @property
    def geomap_icon(self):
        return self.default_icon

    @property
    def geomap_popup_view(self):
        return "<strong>{}</strong>".format(str(self))

    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view

    @property
    def geomap_popup_common(self):
        return self.geomap_popup_view



class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    comment = models.TextField(null=True,blank=True)
    # Add other fields like customer information, shipping details, etc.


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.apartment.name)
