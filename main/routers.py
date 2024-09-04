from rest_framework.routers import DefaultRouter
from django.urls import path

from apartment.views import ApartmentListView, ApartmentDetailView, ApartmentShotsViewSet, OrderView, BrandViewSet,\
                            CityViewSet, DistrictViewSet, CategoryViewSet, ProjectViewSet, FeatureViewSet
from rent_apartment.views import RentApartmentListView, RentApartmentDetailView, RentApartmentShotsViewSet, RentOrderView,\
                                LocationViewSet,ConvenienceViewSet, ConditionViewSet, CharacteristicViewSet
from news_and_banners.views import BannerViewSet, NewsViewSet, AdvertisementView
router = DefaultRouter()
router.register('features', FeatureViewSet,basename='features')
router.register('projects', ProjectViewSet, basename='projects')
router.register('apartment-shots', ApartmentShotsViewSet, basename='apartment-shots')
router.register('brands', BrandViewSet, basename='brands')
router.register('cities', CityViewSet, basename='cities')
router.register('districts', DistrictViewSet, basename='districts')
router.register('categories', CategoryViewSet, basename='categories')
#new_and_banners
router.register('banners', BannerViewSet, basename='banners')
router.register('news', NewsViewSet, basename='news')
# rent_apartments
router.register('rent-apartment-shots', RentApartmentShotsViewSet, basename='rent-apartment-shots')
router.register('locations', LocationViewSet, basename='locations')
router.register('conveniences', ConvenienceViewSet, basename='conveniences')
router.register('conditions', ConditionViewSet, basename='conditions')
router.register('characteristics', CharacteristicViewSet, basename='characteristics')
urlpatterns = router.urls
urlpatterns += [
    path('apartment-list/', ApartmentListView.as_view(), name='apartment-list'),
    path('apartment-detail/<int:pk>/', ApartmentDetailView.as_view(), name='apartment-detail'),
    path('orders/', OrderView.as_view(), name='orders'),
    #rent_apartment
    path('rent-apartment-list/', RentApartmentListView.as_view(), name='rent-apartment-list'),
    path('rent-apartment-detail/<int:pk>/', RentApartmentDetailView.as_view(), name='rent-apartment-detail'),
    path('rent-apartment-order/', RentOrderView.as_view(), name='rent-apartment-order'),
    #new_and_banners
    path('advertisements/', AdvertisementView.as_view(),name='advertisements')
]