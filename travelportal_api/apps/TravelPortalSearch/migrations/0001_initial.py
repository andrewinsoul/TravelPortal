# Generated by Django 2.2.7 on 2019-11-29 11:47

from django.db import migrations, models
import django.db.models.deletion
import travelportal_api.apps.TravelPortalSearch.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('code', models.CharField(max_length=3, validators=[travelportal_api.apps.TravelPortalSearch.models.validate_airport_code])),
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
                ('cabin_class', models.CharField(choices=[('First', 'First Class'), ('Business', 'Business Class'), ('Premium', 'Premium Class'), ('Economy', 'Economy Class'), ('All', 'All Class')], default='All', max_length=54)),
                ('arrival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrive_at_airport', to='TravelPortalSearch.Airport')),
                ('depature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart_from_airport', to='TravelPortalSearch.Airport')),
            ],
        ),
    ]
