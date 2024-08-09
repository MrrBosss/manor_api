from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline

from .models import News, Banner
# Register your models here.

@admin.register(Banner)
class BannerAdmin(TabbedTranslationAdmin):
    list_display = ['text','id']
    list_display_links = ['text','id']
    
@admin.register(News)
class NewsAdmin(TabbedTranslationAdmin):
    list_display = ['id']
    list_display_links = ['id']
    search_fields = ['id']
