from django.db import models
from enum import Enum
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Cabin_Class(Enum):
  F = 'First Class'
  E = 'Economy Class'
  P = 'Premium Class'
  B = 'Business Class'
  A = 'All Class'


def validate_city_code(value:str) -> str:
  if not value.isalpha():
    raise ValidationError(_('%(value) is not a valid code'), params={'value': value})

class City(models.Model):
  name = models.CharField(max_length=90)
  code = models.CharField(max_length=3, validators=[validate_city_code])
  country = models.CharField(max_length=40)

  def __str__(self:object) -> tuple:
    return self.name, self.country

class Flight(models.Model):
  name = models.CharField(max_length=70)
  city = models.ForeignKey(City, on_delete=models.CASCADE)
  price = models.IntegerField()
  departure_date = models.DateTimeField()
  return_date = models.DateTimeField()
  cabin_class = models.CharField(max_length=4, choices=[(class_cat, class_cat.value) for class_cat in Cabin_Class])

  def __str__(self:object) -> tuple:
    return self.name, self.price
