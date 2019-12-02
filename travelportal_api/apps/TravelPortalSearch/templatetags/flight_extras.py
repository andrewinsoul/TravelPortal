from django import template
import datetime

register = template.Library()

@register.filter
def throw_date(value):
  return datetime.datetime.strftime(value, "%Y-%m-%dT%H:%MZ").split('T')[0]

@register.filter
def throw_time(value):
  return datetime.datetime.strftime(value, "%Y-%m-%dT%H:%MZ").split('T')[1].replace('Z', '')

@register.filter
def format_price(value):
  return f'₦{int(value):,}'
