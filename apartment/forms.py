# from django import forms
# from .models import Apartment, Characteristic

# class ApartmentForm(forms.ModelForm):
#     class Meta:
#         model = Apartment
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if 'characteristics' in self.fields:
#             # Filter or customize the queryset for characteristics
#             self.fields['characteristics'].queryset = Characteristic.objects.all()

#         # Optional: Limit the fields to those that are critical
#         self.fields['characteristics'].queryset = Characteristic.objects.values(
#             'total_area',
#             # 'residential_area',
#             # 'floor',
#             # 'year_of_delivery',
#             # You can add more fields if necessary
#         )
