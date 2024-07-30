from django.db import models

# Create your models here.

class RentApartment(models.Model):
    name = models.CharField(max_length=50,null=True)




class RentApartmentShots(models.Model):
    rent_apartment = models.ForeignKey(RentApartment, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='rent-apartments', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Shot for {self.rent_apartment.name}"
    
    class Meta:
        verbose_name = "Ijara turar joy rasmi"
        verbose_name_plural = "Ijara turar joy rasmlari"