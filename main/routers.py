from rest_framework.routers import DefaultRouter
from django.urls import path

from apartment.views import ApartmentListView, ApartmentDetailView, ApartmentShotsViewSet, OrderView


router = DefaultRouter()
router.register('apartment-shots', ApartmentShotsViewSet, basename='apartment-shots')
urlpatterns = router.urls
urlpatterns += [
    path('apartment-list/', ApartmentListView.as_view(), name='apartment-list'),
    path('apartment-detail/<int:pk>/', ApartmentDetailView.as_view(), name='apartment-detail'),
    path('orders/', OrderView.as_view(), name='orders'),
]