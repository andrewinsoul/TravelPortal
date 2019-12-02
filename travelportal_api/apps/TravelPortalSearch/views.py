from django.shortcuts import render
from .models import Flight
from django.http import HttpResponseBadRequest
from django.db.models import Q
from datetime import datetime

def index(request):
  flights = Flight.objects.all()  
  departure_city = request.GET.get('departure_city')
  destination_city = request.GET.get('destination_city')
  departure_date = request.GET.get('departure_date')
  return_date = request.GET.get('return_date')
  cabin = request.GET.get('cabin')
  cabin_class = ['All', 'Business', 'Premium', 'Economy', 'First']
  if departure_city and departure_city is not None:
    flights = flights.filter(
      Q(departure__country__code=departure_city) | 
      Q(departure__country__name=departure_city) |
      Q(departure__city__code=departure_city) |
      Q(departure__city__name=departure_city)
    )
  if destination_city and destination_city is not None:
    flights = flights.filter(
      Q(arrival__country__code=destination_city) | 
      Q(arrival__country__name=destination_city) |
      Q(arrival__city__code=destination_city) |
      Q(arrival__city__name=destination_city)
    )
  if departure_date and departure_date is not None:
    now = datetime.today()
    departure_date = datetime.strptime(departure_date, "%Y-%m-%d")
    delta = departure_date - now
    if departure_date < now or delta.days >= 182.5:
      return HttpResponseBadRequest('<h1>Departure date must be in the future and not greater than 6 months</h1>')
    flights = flights.filter(departure_date=departure_date)

  if return_date and return_date is not None:
    if return_date < departure_date:
      return HttpResponseBadRequest('Return date must be after departure date')
    flights = flights.filter(return_date=return_date)

  if cabin and cabin is not None:
    if cabin not in cabin_class:
      return HttpResponseBadRequest('cabin_class must either be All, Economy, Premium, First, Business')
    flights = flights.filter(cabin_class=cabin)
  context = {'queryset': flights}
  return render(request, 'index.html', context=context)
