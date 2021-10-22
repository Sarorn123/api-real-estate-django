# IMAGE APP FUNCTIONS

from .models import Image
from .serializers import ImageSerializer

def getDiscoverData():
    datas = Image.objects.filter(type = "DISCOVER")
    data = ImageSerializer(datas, many=True)
    return data.data

def getPropertyData():
    datas = Image.objects.filter(type = "PROPERTY")
    data = ImageSerializer(datas, many=True)
    return data.data

def getExploreData():
    datas = Image.objects.filter(type = "EXPLORE")
    data = ImageSerializer(datas, many=True)
    return data.data

def getBackgroundImage():
    datas = Image.objects.get(type = "UI_BACKGRAUD")
    data = ImageSerializer(datas, many=False)
    return data.data