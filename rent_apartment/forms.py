from django import forms
from mapwidgets.widgets import GoogleMapsAddressWidget
import mapwidgets
from .models import Location


class LocationAdminForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['apartment', 'rent_apartment', 'name', 'lon', 'lat']
        widgets = {
            'lon': GoogleMapsAddressWidget,  # Custom widget for longitude and latitude
            'lat': GoogleMapsAddressWidget,
        }
