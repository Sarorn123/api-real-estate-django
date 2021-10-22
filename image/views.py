from .serializers import ImageSerializer, SingleImageSerializer, DocumentSerializer, MaterialSerializer, FeatureSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Image, Document, Material, Feature

from rest_framework import viewsets


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = SingleImageSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


@api_view(['GET'])
def getHouse(request, pk):
    houses = Image.objects.get(id=pk)
    serializer = SingleImageSerializer(houses, many=False)
    json = serializer.data

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
        "house": json,
        "materials": array_data,
        "features": array_data_feature,
        "related_data": related_data,
    }

    return Response({"data": result_data})
