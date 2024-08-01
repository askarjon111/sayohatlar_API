from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.tours.models import Category, Country, Destination, Tour
from apps.tours.serializers import CategorySerializer, CountrySerializer, DestinationSerializer, RestaurantSerializer, TourSerializer


@api_view(['GET'])
def featured_categories_view(request):
    categories = Category.objects.all()[:5]
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, 200)


@api_view(['GET'])
def featured_countries_view(request):
    countries = Country.objects.all()[:3]
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data, 200)


@api_view(['GET'])
def featured_destinations_view(request):
    destinations = Destination.objects.all()[:10]
    serializer = DestinationSerializer(destinations, many=True)
    return Response(serializer.data, 200)



@api_view(['GET'])
def featured_restaurants_view(request):
    restaurants = Destination.objects.all()[:10]
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data, 200)


@api_view(['GET'])
def tours_by_destination_view(request, pk):
    destination = Destination.objects.get(id=pk)
    tours = Tour.objects.filter(destinations__in=[destination])
    serializer = TourSerializer(tours, many=True)
    return Response(serializer.data, 200)
