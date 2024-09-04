from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import News, Banner, Advertisement
# Register your models here.

@admin.register(Banner)
class BannerAdmin(TabbedTranslationAdmin):
    list_display = ['text_uz','id']
    list_display_links = ['text_uz','id']
    
@admin.register(News)
class NewsAdmin(TabbedTranslationAdmin):
    list_display = ['content_uz','id']
    list_display_links = ['content_uz','id']
    search_fields = ['id']

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['name','order_date','id']
    list_display_links = ['name','order_date','id']