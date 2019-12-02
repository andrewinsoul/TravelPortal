from django.urls import path
from travelportal_api.apps.TravelPortalSearch import views

urlpatterns = [
    path('', views.index, name='index'),
]
