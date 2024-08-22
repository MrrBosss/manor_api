from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from .models import Apartment, Category, Characteristic
from rent_apartment.models import RentApartment, Convenience, Condition
from news_and_banners.models import News, Banner

@register(Apartment)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','description')

@register(Characteristic)
class CharacteristicTranslationOptions(TranslationOptions):
    fields = ('house','finishing','view_from_window','type')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(RentApartment)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','description')

@register(Convenience)
class ConvenienceTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Condition)
class ConditionTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('content',)

@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('text',)