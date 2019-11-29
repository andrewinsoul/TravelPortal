from django_seed import Seed
from django.core.management.base import BaseCommand
from django.utils import timezone
import string
from travelportal_api.apps.TravelPortalSearch.models import Airport, Flight
import random

seeder = Seed.seeder();

class Command(BaseCommand):
  help = 'seed database'

  def handle(self, *args, **kwargs):
    seeder.add_entity(Airport, 30, {
      'name': lambda x: seeder.faker.city(),
      'code': lambda x: ''.join(random.choice(string.ascii_uppercase) for _ in range(3)),
      'country': lambda x: seeder.faker.country()
    })

    category = ["All", "Economy", "Business", "First", "Premium"]
    random_category_index = random.randint(0, 4)
    seeder.add_entity(Flight, 150, {
      'name': lambda x: seeder.faker.word(),
      'price': lambda x: random.randint(1, 9) * 200000,
      'cabin_class': lambda x: category[random_category_index]
    })

    seeder.execute()
