from .serializers import ImageSerializer, SingleImageSerializer, DocumentSerializer, MaterialSerializer, FeatureSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Image, Document, Material, Feature
from systemUser.models import AccessModule, TitleUI
from systemUser.serializers import AccessModuleSerializer, TitleUISerializer
from .functions import *
from agency.functions import *


from rest_framework import viewsets


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = SingleImageSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


@api_view(['GET'])
def getMenuTree(request):
    access = AccessModule.objects.all()
    serializer = AccessModuleSerializer(access, many=True)
    menu_tree = serializer.data

    return Response({"data": menu_tree})


@api_view(['GET'])
def getPropertyTree(request):

    access = AccessModule.objects.filter(user_type = "USER")
    serializer = AccessModuleSerializer(access, many=True)
    menu_tree = serializer.data

    ui = TitleUI.objects.get(id=1)
    ui2 = TitleUI.objects.get(id=2)
    uiSerializer = TitleUISerializer(ui, many=False)
    ui2Serializer = TitleUISerializer(ui2, many=False)
    uiData = uiSerializer.data
    uiData2 = ui2Serializer.data
    uiData2 = uiData2['name']
    uiData = uiData['name']

    discover = getDiscoverData()
    property = getPropertyData()
    explore = getExploreData()
    agency = getAllAgencys()
    employee = getAllAgencyEmployees()
    bg_image = getBackgroundImage()

    data = {
        'menu_tree': menu_tree,
        'title_1': uiData,
        'title_2': uiData2,
        'background_image': bg_image['image_url'],
        'discover_data': discover,
        'explore_property': property,
        'explore_property_city': explore,
        'recommend_agency': agency,
        "feature_agency": employee,
    }

    return Response({"data": data})


@api_view(['GET'])
def getHouse(request, pk):
    houses = Image.objects.get(id=pk)
    serializer = SingleImageSerializer(houses, many=False)
    json = serializer.data

    access = AccessModule.objects.filter(user_type="USER")
    serializer = AccessModuleSerializer(access, many=True)
    menu_tree = serializer.data

    # MATERIAL

    materials = json['materials_ids']
    material = materials.split(',')
    array_data = []
    if material != [""]:
        for x in material:
            try:
                mat = Material.objects.get(id=x)
                serializer = MaterialSerializer(mat, many=False)
                array_data.append(serializer.data)
            except:
                return Response({"message": "Some material is not found!"})

    # FEATURE

    features = json['feature_ids']
    feature = features.split(',')

    array_data_feature = []
    if feature != [""]:
        for y in feature:
            try:
                mat = Feature.objects.get(id=y)
                serializer = FeatureSerializer(mat, many=False)
                array_data_feature.append(serializer.data)
            except:
                return Response({"message": "Some feature is not found!"})

    # RELATED ITEM

    relateds = json['related_item']
    related = relateds.split(',')

    related_data = []
    if related != [""]:
        for y in related:
            try:
                mat = Image.objects.get(id=y)
                serializer = ImageSerializer(mat, many=False)
                related_data.append(serializer.data)
            except:
                return Response({"message": "Some feature is not found!"})

    result_data = {
        "menu_data": menu_tree,
        "house": json,
        "materials": array_data,
        "features": array_data_feature,
        "related_data": related_data,
    }

    return Response({"data": result_data})
