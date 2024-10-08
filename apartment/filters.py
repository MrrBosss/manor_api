import django_filters
from .models import Apartment, City, District, Brand, Category

class ApartmentFilter(django_filters.FilterSet):
    city = django_filters.ModelChoiceFilter(queryset=City.objects.all())
    district = django_filters.ModelChoiceFilter(queryset=District.objects.all())
    brand = django_filters.ModelChoiceFilter(queryset=Brand.objects.all())
    room = django_filters.NumberFilter(lookup_expr='exact')
    price_lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    price_gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    mortgage_available = django_filters.BooleanFilter(field_name='mortgage_available', lookup_expr='exact')
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget=django_filters.widgets.CSVWidget)

    class Meta:
        model = Apartment
        fields = ['city','district','brand','room','price_lte','price_gte','mortgage_available','category']

