from django.db import models

# Create your models here.

class RentApartment(models.Model):
    name = models.CharField(max_length=50,null=True)
    price_per_m = models.FloatField(default=1.000)
    apartment = models.IntegerField(default=2)
    tenant_name = models.CharField(max_length=50, null=True)
    tenant_image = models.ImageField(upload_to='images', null=True, blank=True)
    company = models.CharField(max_length=50, null=True)
    total_area = models.FloatField(default=0)
    residential_are = models.FloatField(default=0)
    floor = models.IntegerField(default=0)
    year_of_delivery = models.IntegerField(default=0)
    house = models.CharField(max_length=100,null=True)
    finishing = models.CharField(max_length=100)
    viev_from_window = models.CharField(max_length=100)
    bathroom = models.IntegerField(default=0)
    type = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.name)


class RentApartmentShots(models.Model):
    rent_apartment = models.ForeignKey(RentApartment, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='rent-apartments', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Shot for {self.rent_apartment.name}"


class RentApartmentOrder(models.Model):
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    comment = models.TextField(null=True,blank=True)
    # Add other fields like customer information, shipping details, etc.


class RentApartmentOrderItem(models.Model):
    order = models.ForeignKey(RentApartmentOrder, related_name='items', on_delete=models.CASCADE)
    apartment = models.ForeignKey(RentApartment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.apartment.name)
