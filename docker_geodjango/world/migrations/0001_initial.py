# Generated by Django 4.2.2 on 2023-07-01 12:25

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorldBorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('pop2005', models.IntegerField(blank=True, null=True, verbose_name='Population 2005')),
                ('fips', models.CharField(blank=True, max_length=2, null=True, verbose_name='FIPS Code')),
                ('iso2', models.CharField(blank=True, max_length=2, null=True, verbose_name='2 Digit ISO')),
                ('iso3', models.CharField(blank=True, max_length=3, null=True, verbose_name='3 Digit ISO')),
                ('un', models.IntegerField(blank=True, null=True, verbose_name='United Nations Code')),
                ('region', models.IntegerField(blank=True, null=True, verbose_name='Region Code')),
                ('subregion', models.IntegerField(blank=True, null=True, verbose_name='Sub-Region Code')),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('mpoly', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
        ),
    ]
