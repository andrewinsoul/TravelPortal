# Generated by Django 2.2.7 on 2019-11-29 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TravelPortalSearch', '0004_airport_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='depature',
            new_name='departure',
        ),
    ]