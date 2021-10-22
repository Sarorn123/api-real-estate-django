from .models import Agency, AgencyEmployee
from rest_framework import serializers


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = "__all__"

class AgencyEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgencyEmployee
        fields = "__all__"
