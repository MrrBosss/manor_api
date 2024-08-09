from django.contrib import admin

from .models import News, Banner
# Register your models here.

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['text','id']
    list_display_links = ['text','id']
    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']
    search_fields = ['id']
