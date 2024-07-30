from rest_framework.routers import DefaultRouter
from django.urls import path

from apartment.views import ApartmentListView, ApartmentDetailView, ApartmentShotsViewSet, OrderView
from rent_apartment.views import RentApartmentListView, RentApartmentDetailView, RentApartmentShotsViewSet, RentOrderView

router = DefaultRouter()
router.register('apartment-shots', ApartmentShotsViewSet, basename='apartment-shots')
router.register('rent-apartment-shots', RentApartmentShotsViewSet, basename='rent-apartment-shots')
urlpatterns = router.urls
urlpatterns += [
    path('apartment-list/', ApartmentListView.as_view(), name='apartment-list'),
    path('apartment-detail/<int:pk>/', ApartmentDetailView.as_view(), name='apartment-detail'),
    path('orders/', OrderView.as_view(), name='orders'),
    path('rent-apartment-list/', RentApartmentListView.as_view(), name='rent-apartment-list'),
    path('rent-apartment-detail/<int:pk>/', RentApartmentDetailView.as_view(), name='rent-apartment-detail'),
    path('rent-apartment-order/', RentOrderView.as_view(), name='rent-apartment-order')
]