# Generated by Django 2.2.7 on 2019-11-29 05:03

from django.db import migrations, models
import django.db.models.deletion
import travelportal_api.apps.TravelPortalSearch.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('code', models.CharField(max_length=3, validators=[travelportal_api.apps.TravelPortalSearch.models.validate_city_code])),
                ('country', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('price', models.IntegerField()),
                ('departure_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('cabin_class', models.CharField(choices=[(travelportal_api.apps.TravelPortalSearch.models.Cabin_Class('First Class'), 'First Class'), (travelportal_api.apps.TravelPortalSearch.models.Cabin_Class('Economy Class'), 'Economy Class'), (travelportal_api.apps.TravelPortalSearch.models.Cabin_Class('Premium Class'), 'Premium Class'), (travelportal_api.apps.TravelPortalSearch.models.Cabin_Class('Business Class'), 'Business Class'), (travelportal_api.apps.TravelPortalSearch.models.Cabin_Class('All Class'), 'All Class')], max_length=4)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TravelPortalSearch.City')),
            ],
        ),
    ]