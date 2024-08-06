from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.tours.views import TourViewSet, featured_categories_view, featured_countries_view, featured_destinations_view, featured_restaurants_view, hotel_detail_view, tour_detail_view, tour_list_view, tours_by_destination_view

router = DefaultRouter()
router.register(r'tours', TourViewSet, basename='tour')

urlpatterns = [
    path('featured-categories/', featured_categories_view,
         name='featured_categories'),
    path('featured-countries/', featured_countries_view, name='featured_countries'),
    path('featured-destinations/', featured_destinations_view,
         name='featured_destinations'),
    path('featured-restaurants/', featured_restaurants_view,
         name='featured_restaurants'),
    path('destinations/<int:pk>/', tours_by_destination_view,
         name='tours_by_destination'),
    path('tours/<int:pk>/', tour_detail_view,
         name='tour_detail'),
    path('hotels/<int:pk>/', hotel_detail_view,
         name='hotel_detail'),
#     path('tours/', tour_list_view, name='tour_list'),
]

urlpatterns += router.urls