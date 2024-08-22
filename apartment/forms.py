from dal import autocomplete
from django import forms
from .models import Apartment, Project

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'
        widgets = {
            'project': autocomplete.ModelSelect2(url='project-autocomplete', forward=['brand']),
        }