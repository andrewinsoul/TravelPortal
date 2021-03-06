# Generated by Django 2.2.7 on 2019-11-29 12:33

from django.db import migrations, models
import travelportal_api.apps.TravelPortalSearch.models


class Migration(migrations.Migration):

    dependencies = [
        ('TravelPortalSearch', '0003_airport_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='code',
            field=models.CharField(max_length=3, validators=[travelportal_api.apps.TravelPortalSearch.models.validate_airport_code]),
            preserve_default=False,
        ),
    ]
