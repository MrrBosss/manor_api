from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import Apartment, Category
from rent_apartment.models import RentApartment

@register(Apartment)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','description','type','view_from_window','finishing','house')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(RentApartment)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','description','type','view_from_window','finishing','house')