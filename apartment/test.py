from django.test import TestCase
from .models import Location

class LocationModelTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            name="Test Location",
            lon=12.34,
            lat=56.78
        )

    def test_geomap_longitude(self):
        self.assertEqual(self.location.geomap_longitude, "12.34")

    def test_geomap_latitude(self):
        self.assertEqual(self.location.geomap_latitude, "56.78")

    def test_geomap_icon(self):
        # Add logic to test the default_icon if set
        self.assertEqual(self.location.geomap_icon, self.location.default_icon)

    def test_geomap_popup_view(self):
        self.assertEqual(self.location.geomap_popup_view, "<strong>Test Location</strong>")

    def test_geomap_popup_edit(self):
        self.assertEqual(self.location.geomap_popup_edit, "<strong>Test Location</strong>")

    def test_geomap_popup_common(self):
        self.assertEqual(self.location.geomap_popup_common, "<strong>Test Location</strong>")
