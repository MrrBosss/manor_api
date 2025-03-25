import django_filters
from .models import Apartment, City, District, Brand, Category

class ApartmentFilter(django_filters.FilterSet):
    city_id = django_filters.ModelChoiceFilter(queryset=City.objects.all())
    district_id = django_filters.ModelChoiceFilter(queryset=District.objects.all())
    brand_id = django_filters.ModelChoiceFilter(queryset=Brand.objects.all())
    rooms = django_filters.NumberFilter(lookup_expr='exact', field_name='room')
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    price_from = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    mortgage_available = django_filters.BooleanFilter(field_name='mortgage_available', lookup_expr='exact')
    category_id = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), 
                                                           widget=django_filters.widgets.CSVWidget)

    class Meta:
        model = Apartment
        fields = ['city_id','district_id','brand_id','rooms','price_to','price_from','mortgage_available','category_id']
