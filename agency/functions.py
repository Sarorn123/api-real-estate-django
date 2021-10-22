# AGENCY FUNCTION

from .models import Agency, AgencyEmployee
from .serializers import AgencyEmployeeSerializer, AgencyEmployeeSerializer, AgencySerializer


def getAllAgencys():
    data = Agency.objects.all()
    serializer = AgencySerializer(data, many=True)
    return serializer.data

def getAllAgencyEmployees():
    data = AgencyEmployee.objects.all()
    serializer = AgencyEmployeeSerializer(data, many=True)
    return serializer.data