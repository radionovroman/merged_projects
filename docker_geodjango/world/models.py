from django.contrib.gis.db import models


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50, null= True, blank= True)
    area = models.IntegerField(null= True, blank= True)
    pop2005 = models.IntegerField('Population 2005', null= True, blank= True)
    fips = models.CharField('FIPS Code', max_length=2, blank=True, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2, null= True, blank= True)
    iso3 = models.CharField('3 Digit ISO', max_length=3, null= True, blank= True)
    un = models.IntegerField('United Nations Code', null= True, blank= True)
    region = models.IntegerField('Region Code', null= True, blank= True)
    subregion = models.IntegerField('Sub-Region Code', null= True, blank= True)
    lon = models.FloatField(null= True, blank= True)
    lat = models.FloatField(null= True, blank= True)

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.GeometryField(null=True, blank=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name