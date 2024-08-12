from django.db import models
from apartment.validators import validate_image_or_video
# Create your models here.


class News(models.Model):
    media = models.FileField(upload_to='news', null=True,blank=True, validators=[validate_image_or_video])
    content = models.TextField(null=True, blank=True)


class Banner(models.Model):
    text = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='banners',null=True)