from django.db import models
from apartment.validators import validate_image_or_video
# Create your models here.


class News(models.Model):
    media = models.FileField(upload_to="Media", null=True,blank=True, validators=[validate_image_or_video])
    content = models.TextField("Matn",null=True, blank=True)

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'


class Banner(models.Model):
    alias = models.URLField("Link",null=True,blank=True)
    text = models.CharField("Matn",max_length=500, null=True,blank=True)
    image = models.ImageField("Rasm",upload_to='banners',null=True,blank=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlar"