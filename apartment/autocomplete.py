# in yourapp/autocomplete.py
from dal import autocomplete
from django import forms
from .models import Project

class ProjectAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Filter by the brand if one is selected
        brand_id = self.forwarded.get('brand', None)
        if brand_id:
            return Project.objects.filter(brand_id=brand_id).order_by('id')
        return Project.objects.none()
