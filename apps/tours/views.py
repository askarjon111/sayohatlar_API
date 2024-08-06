from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.tours.models import Category, Country, Destination, Hotel, Tour
from apps.tours.serializers import CategorySerializer, CountrySerializer, DestinationSerializer, HotelSerializer, RestaurantSerializer, TourSerializer


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


@api_view(['GET'])
def tour_list_view(request):
    tours = Tour.objects.all()
    category = request.GET.get('category')
    destination = request.GET.get('destination')
    country = request.GET.get('country')

    if category:
        category = Category.objects.get(id=category)
        tours = tours.filter(categories__in=[category,])
    if destination:
        destination = Destination.objects.get(id=destination)
        tours = tours.filter(destinations__in=[destination,])
    if country:
        country = Country.objects.get(id=country)
        tours = tours.filter(countries__in=[country,])

    serializer = TourSerializer(tours, many=True)

    return Response(serializer.data, 200)

@api_view(['GET'])
def tour_detail_view(request, pk):
    tour = Tour.objects.get(id=pk)
    serializer = TourSerializer(tour)

    return Response(serializer.data, 200)


@api_view(['GET'])
def hotel_detail_view(request, pk):
    hotel = Hotel.objects.get(id=pk)
    serializer = HotelSerializer(hotel)

    return Response(serializer.data, 200)


class TourViewSet(viewsets.ViewSet):
    def list(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data, 200)

    def retrieve(self, request, pk=None):
        tours = Tour.objects.get(pk=pk)
        serializer = TourSerializer(tours)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        tour = Tour.objects.get(pk=pk).delete()
        return Response(status=204)