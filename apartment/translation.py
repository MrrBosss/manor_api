from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from .models import Apartment, Category, Characteristic, Features
from rent_apartment.models import RentApartment, Convenience, Condition
from news_and_banners.models import News, Banner

# Apartments
@register(Apartment)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','description')

@register(Features)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(Characteristic)
class CharacteristicTranslationOptions(TranslationOptions):
    fields = ('house','finishing','view_from_window','type')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

# Rent Apartments
@register(RentApartment)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','description')

@register(Convenience)
class ConvenienceTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Condition)
class ConditionTranslationOptions(TranslationOptions):
    fields = ('name',)

#News And others
@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('content',)

@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('text',)