from django.urls import path
from travelportal_api.apps.TravelPortalSearch import views

urlpatterns = [
    path('v1/flight/search-flight', views.FlightList.as_view()),
]
