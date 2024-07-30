from rest_framework import serializers

from apps.tours.models import Category, Country, Destination


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    destinations_count = serializers.SerializerMethodField()

    def get_destinations_count(self, obj):
        return obj.destination_set.count()

    class Meta:
        model = Country
        fields = ['id', 'image', 'name', 'destinations_count']


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
