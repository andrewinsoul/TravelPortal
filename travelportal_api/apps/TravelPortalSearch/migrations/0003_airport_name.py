# Generated by Django 2.2.7 on 2019-11-29 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravelPortalSearch', '0002_auto_20191129_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='name',
            field=models.CharField(max_length=90),
            preserve_default=False,
        ),
    ]
