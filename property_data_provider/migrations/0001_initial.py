# Generated by Django 3.1.7 on 2021-03-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetPropertyRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('air_conditioning', models.CharField(max_length=100)),
                ('attic', models.BooleanField()),
                ('basement', models.CharField(max_length=100)),
                ('building_area_sq_ft', models.IntegerField()),
                ('building_condition_score', models.IntegerField()),
                ('building_quality_score', models.IntegerField()),
                ('construction_type', models.CharField(max_length=100)),
                ('exterior_walls', models.CharField(max_length=100)),
                ('fireplace', models.BooleanField(max_length=100)),
                ('full_bath_count', models.IntegerField()),
                ('garage_parking_of_cars', models.IntegerField()),
                ('garage_type_parking', models.CharField(max_length=100)),
                ('heating', models.CharField(max_length=100)),
                ('no_of_buildings', models.IntegerField()),
                ('no_of_stories', models.IntegerField()),
                ('number_of_bedrooms', models.IntegerField()),
                ('number_of_units', models.IntegerField()),
                ('partial_bath_count', models.IntegerField()),
                ('pool', models.BooleanField()),
                ('property_type', models.CharField(max_length=100)),
                ('roof_cover', models.CharField(max_length=100)),
                ('roof_type', models.CharField(max_length=100)),
                ('sewer', models.CharField(max_length=100)),
                ('site_area_acres', models.BigIntegerField()),
                ('style', models.CharField(max_length=100)),
                ('subdivision', models.CharField(max_length=100)),
                ('total_bath_count', models.IntegerField()),
                ('water', models.CharField(max_length=100)),
                ('year_built', models.IntegerField()),
                ('zoning', models.CharField(max_length=100)),
            ],
        ),
    ]
