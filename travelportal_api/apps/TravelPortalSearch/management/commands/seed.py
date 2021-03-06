from django_seed import Seed
from django.core.management.base import BaseCommand
from django.utils import timezone
import string
from datetime import datetime
from travelportal_api.apps.TravelPortalSearch.models import Airport, Flight, City, Country
import random

seeder = Seed.seeder();

class Command(BaseCommand):
  help = 'seed database'

  def handle(self, *args, **kwargs):
    seeder.add_entity(City, 20, {
      'code': lambda x: ''.join(random.choice(string.ascii_uppercase) for _ in range(3)),
      'name': lambda x: seeder.faker.city()
    })

    seeder.add_entity(Country, 30, {
      'code': lambda x: ''.join(random.choice(string.ascii_uppercase) for _ in range(3)),
      'name': lambda x: seeder.faker.country()
    })
    
    seeder.add_entity(Airport, 40, {
      'name': lambda x: seeder.faker.name(),
      'code': lambda x: ''.join(random.choice(string.ascii_uppercase) for _ in range(3)),
    })

    category = ["All", "Economy", "Business", "First", "Premium"]
    random_category_index = random.randint(0, 4)
    seeder.add_entity(Flight, 150, {
      'name': lambda x: seeder.faker.word().title(),
      'price': lambda x: random.randint(1, 9) * 200000,
      'cabin_class': lambda x: category[random_category_index],
      'departure_date': lambda x: seeder.faker.date_time_between_dates(
        datetime_start=datetime.strptime('2019-12-05T10:12:50Z', '%Y-%m-%dT%H:%M:%SZ'),
        datetime_end=datetime.strptime('2020-06-03T12:00:32Z', '%Y-%m-%dT%H:%M:%SZ')
      ),
      'return_date': lambda x: seeder.faker.date_time_between_dates(
        datetime_start=datetime.strptime('2020-07-03T12:00:32Z', '%Y-%m-%dT%H:%M:%SZ'),
        datetime_end=datetime.strptime('2021-06-03T12:00:32Z', '%Y-%m-%dT%H:%M:%SZ')
      )
    })

    seeder.execute()
