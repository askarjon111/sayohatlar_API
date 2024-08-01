from django.urls import path

from apps.tours.views import featured_categories_view, featured_countries_view, featured_destinations_view, featured_restaurants_view, tour_detail_view, tours_by_destination_view


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
]
