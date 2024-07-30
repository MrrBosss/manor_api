from django.db import models

# Create your models here.

class Apartment(models.Model):
    name = models.CharField(max_length=50,null=True)
    company_logo = models.ImageField(upload_to='logos',null=True)
    company_name = models.CharField(max_length=50,null=True)
    price = models.FloatField(default=10.000)
    price_per_m = models.FloatField(default=1.000)
    apartment_sold = models.IntegerField(default=0)
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
    is_finish = models.BooleanField(default=False)



class ApartmentShots(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Shot for {self.apartment.name}"


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
