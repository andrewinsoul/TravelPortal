from django.shortcuts import render,render_to_response
from .models import Flight
from rest_framework.response import Response
from .serializers import FlightSerializer
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime


class FlightList(APIView):
  def get(self, request, format=None):
    query_param = self.request.query_params.keys()
    allowed_query_params = ['departure_city', 'destination_city', 'departure_date', 'return_date', 'cabin', 'calendar', 'preferred']
    cabin_class = ['All', 'Business', 'Premium', 'Economy', 'First']
    for param in query_param:
      if param not in allowed_query_params:
        return Response({'error': 'invalid query parameter {} provided'.format(param)}, 400)
    departure_city = self.request.query_params.get('departure_city')
    destination_city = self.request.query_params.get('destination_city')
    departure_date = self.request.query_params.get('departure_date')
    cabin = self.request.query_params.get('cabin')
    return_date = self.request.query_params.get('return_date')
    calendar = self.request.query_params.get('calendar')
    preferred = self.request.query_params.get('preferred')
    
    if departure_city is not None:
      if len(departure_city) != 3 or not departure_city.isalpha():
        return Response(
          {'error': '{} not a valid code'.format(param)},
          status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    
    if destination_city is not None:
      if len(destination_city) != 3 or not destination_city.isalpha():
        return Response(
          {'error': '{} not a valid code'.format(param)},
          status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    
    if departure_date is not None:
      now = datetime.today()
      departure_date = datetime.strptime(departure_date, '%Y-%m-%d %H:%M:%S 01')
      delta = departure_date - now
      if departure_date < now or delta.days >= 182.5:
        return Response(
          {'error': 'Departure date must be in the future and not greater than 6 months'},
          status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    
    if return_date is not None:
      return_date = datetime.strptime(return_date, '%Y-%m-%d %H:%M:%S 01')
      if return_date < departure_date:
        return Response(
          {'error': 'Return date must be after date of departure'},
          status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    if cabin is not None:
      if cabin.title() not in cabin_class:
        return Response(
          {'error': 'value of cabin query parameter must either be [All, Business, First, Premium, Economy]'},
          status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    if len(query_param) == 0:
      flights = Flight.objects.all()
      serializer = FlightSerializer(flights, many=True)
      return Response(serializer.data)

    flights = Flight.objects.filter(
      departure__city__code=departure_city,
      arrival__city__code=destination_city,
      departure_date=departure_date,
      return_date=return_date,
      cabin_class=cabin
    )
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)
