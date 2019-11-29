from .models import Flight, Airport, City, Country
from rest_framework import serializers
from rest_framework.response import Response


class CitySerializer(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = ['code', 'name']


class CountrySerializer(serializers.ModelSerializer):
  class Meta:
    model = Country
    fields = ['code', 'name']


class AirportSerializer(serializers.ModelSerializer):
  country = CountrySerializer(read_only=True)
  city = CitySerializer()
  class Meta:
    model = Airport
    fields = ['code', 'name', 'country', 'city']


class FlightSerializer(serializers.ModelSerializer):
  departure = AirportSerializer(read_only=True)
  arrival = AirportSerializer(read_only=True)
  class Meta:
    model = Flight
    fields = ['name', 'departure', 'arrival', 'price', 'departure_date', 'return_date', 'cabin_class']
