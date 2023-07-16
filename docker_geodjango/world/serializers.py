from pyexpat import model

from .models import WorldBorder
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class WorldBorderSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WorldBorder
        fields = "__all__"
        geo_field = "mpoly"


# make all fields optional
def to_internal_value(self, data):
    for field_name in self.fields.keys():
        if field_name not in data:
            data[field_name] = None
    return super().to_internal_value(data)
