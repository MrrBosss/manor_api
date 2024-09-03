from django.db import models
import datetime
# Create your models here.


def upload_to(instance, filename):
    # Generate filename here
    if instance.created_at:
        date_str = instance.created_at.strftime("%Y/%m/%d")
    else:
        date_str = datetime.datetime.now().strftime("%Y/%m/%d") # Or use any default date

    return f'{date_str}/{filename}'


class Category(models.Model):
    name = models.CharField("Categoriya",max_length=50,null=True,blank=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Brand(models.Model):
    name = models.CharField("Brend",max_length=100, null=True,blank=True)
    apartment_sold = models.IntegerField("Sotilgan Uylar",default=0,null=True, blank=True)
    year_join = models.IntegerField("Yil",default=0,null=True,blank=True)
    brand_image = models.ImageField("Brend Logosi",upload_to='brand-images', blank=True)
   
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brendlar"


class Project(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField("Proyekt",max_length=50,null=True,blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Proyekt"
        verbose_name_plural = "Proyektlar"


class City(models.Model):
    name = models.CharField("Shahar",max_length=50,null=True)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Shahar"
        verbose_name_plural = "Shaharlar"


class District(models.Model):
    name = models.CharField("Tuman",max_length=50, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "Tumanlar"


class Features(models.Model):
    text = models.CharField("Matn",max_length=500,null=True,blank=True)
    image = models.ImageField("Rasm",upload_to='Features',null=True,blank=True)

    class Meta:
        verbose_name = "Xususiyat"
        verbose_name_plural = "Xususiyatlar"

    def __str__(self):
        return str(self.text)


class Apartment(models.Model):
    name = models.CharField("Nomi",max_length=50,null=True, blank=True)
    price = models.FloatField("Narx",default=10.000,null=True, blank=True)
    price_per_m = models.FloatField("Narx kv metr",default=1.000,null=True, blank=True)
    description = models.TextField("Ta'rif",null=True, blank=True)
    room = models.IntegerField("Xonalar soni",null=True,blank=True)
    mortgage_available = models.BooleanField("Ipoteka",default=False,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    feature = models.ManyToManyField(Features,blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True,blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Turar joy"
        verbose_name_plural = "Turar joylar"


class ApartmentShots(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE,related_name='apartment_shots',null=True,blank=True)
    image = models.ImageField(upload_to=upload_to, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Shot for {self.apartment.name}"
    
    class Meta:
        verbose_name = "Turar joy rasmi"
        verbose_name_plural = "Turar joy rasmlari"


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField("Ism",max_length=100, null=True)
    phone_number = models.CharField("Telefon raqam",max_length=20, null=True)
    comment = models.TextField("Izoh",null=True,blank=True)
    # Add other fields like customer information, shipping details, etc.

    class Meta:
        verbose_name = "Zakaz"
        verbose_name_plural = "Zakazlar"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.apartment.name)
