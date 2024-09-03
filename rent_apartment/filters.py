import django_filters
from .models import RentApartment
from apartment.models import City, District, Brand, Category

class RentApartmentFilter(django_filters.FilterSet):
    city = django_filters.ModelChoiceFilter(queryset=City.objects.all())
    district = django_filters.ModelChoiceFilter(queryset=District.objects.all())
    brand = django_filters.ModelChoiceFilter(queryset=Brand.objects.all())
    room = django_filters.NumberFilter(lookup_expr='exact')
    price_lte = django_filters.NumberFilter(field_name='price_per_m', lookup_expr='lte')
    price_gte = django_filters.NumberFilter(field_name='price_per_m', lookup_expr='gte')
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget=django_filters.widgets.CSVWidget)
    
    class Meta:
        model = RentApartment
        fields = ['city', 'district', 'brand', 'room', 'price_lte', 'price_gte','category']
