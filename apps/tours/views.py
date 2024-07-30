from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.tours.models import Category
from apps.tours.serializers import CategorySerializer


@api_view(['GET'])
def featured_categories_view(request):
    categories = Category.objects.all()[:5]
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, 200)
