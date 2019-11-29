from django.db import models
from enum import Enum
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_airport_code(value:str) -> str:
  if not value.isalpha():
    raise ValidationError(_('%(value) is not a valid code'), params={'value': value})

class Country(models.Model):
  name = models.CharField(max_length=90)
  code = models.CharField(max_length=3, validators=[validate_airport_code])

  def __str__(self:object) -> tuple:
    return self.name, self.code

class City(models.Model):
  name = models.CharField(max_length=90)
  code = models.CharField(max_length=3, validators=[validate_airport_code])
  def __str__(self:object) -> tuple:
    return self.name, self.code

class Airport(models.Model):
  name = models.CharField(max_length=90)
  country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')
  city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')
  code = models.CharField(max_length=3, validators=[validate_airport_code])
  def __str__(self:object) -> tuple:
    return self.name, self.country

class Flight(models.Model):
  Cabin_Class = (
    ('First', 'First Class'),
    ('Business', 'Business Class'),
    ('Premium', 'Premium Class'),
    ('Economy', 'Economy Class'),
    ('All', 'All Class')
  )
  name = models.CharField(max_length=70)
  departure = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='depart_from_airport')
  arrival = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrive_at_airport')
  price = models.IntegerField()
  departure_date = models.DateTimeField()
  return_date = models.DateTimeField()
  cabin_class = models.CharField(max_length=54, choices=Cabin_Class, default='All')
  def __str__(self:object) -> tuple:
    return self.name, self.price
