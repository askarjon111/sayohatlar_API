from django.urls import path

from apps.tours.views import featured_categories_view


urlpatterns = [
    path('featured-categories/', featured_categories_view, name='featured_categories'),
]

