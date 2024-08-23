from django.db import models
import datetime
from django.contrib.gis.db.models import PointField

from apartment.models import Brand, City, District, Category, Apartment, Characteristic
# Create your models here.


def upload_to(instance, filename):
    # Generate filename here
    if instance.created_at:
        date_str = instance.created_at.strftime("%Y/%m/%d")
    else:
        date_str = datetime.datetime.now().strftime("%Y/%m/%d")
  # Or use any default date

    return f'{date_str}/{filename}'


class Convenience(models.Model):
    name = models.CharField("Qulaylik",max_length=50, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Qulaylik"
        verbose_name_plural = "Qulayliklar"


class Condition(models.Model):
    name = models.CharField("Sharoit",max_length=50, null=True,blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Sharoit"
        verbose_name_plural = "Sharoitlar"


class RentApartment(models.Model):
    name = models.CharField("Nomi",max_length=50, null=True, blank=True)
    price_per_m = models.FloatField("Ijara narxi",default=1.000, null=True, blank=True)
    tenant_name = models.CharField("Ismi",max_length=50, null=True, blank=True)
    tenant_image = models.ImageField("Surati",upload_to=upload_to, null=True, blank=True)
    apartment_sold = models.IntegerField("Turar joy",default=0,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField("Ta'rif",null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    convenience = models.ForeignKey(Convenience,on_delete=models.CASCADE,null=True,blank=True)
    condition = models.ForeignKey(Condition,on_delete=models.CASCADE,null=True,blank=True)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Ijara turar joy'
        verbose_name_plural = 'Ijara turar joylar'


class RentApartmentShots(models.Model):
    rent_apartment = models.ForeignKey(RentApartment, on_delete=models.CASCADE,related_name="rent_shots", null=True, blank=True)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Shot for {self.rent_apartment.name}"

    class Meta:
        verbose_name = 'Ijara turar joy rasmi'
        verbose_name_plural = 'Ijara turar joy rasmlari'


class Location(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.Case, null=True, blank=True)
    rent_apartment = models.ForeignKey(RentApartment, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField("Manzil nomi",max_length=100, null=True, blank=True)
    location = PointField("Manzil", geography=True, null=True,blank=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Manzil'
        verbose_name = 'Manzillar'


class RentApartmentOrder(models.Model):
    order_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    name = models.CharField("Ism",max_length=100, null=True, blank=True)
    phone_number = models.CharField("Telefon raqam",max_length=20, null=True, blank=True)
    comment = models.TextField("Izoh",null=True,blank=True)
    # Add other fields like customer information, shipping details, etc.

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Ijara turar joy zakaz'
        verbose_name_plural = 'Ijara turar joy zakazlari'

class RentApartmentOrderItem(models.Model):
    order = models.ForeignKey(RentApartmentOrder, related_name='items', on_delete=models.CASCADE, null=True, blank=True)
    apartment = models.ForeignKey(RentApartment, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.apartment.name)
