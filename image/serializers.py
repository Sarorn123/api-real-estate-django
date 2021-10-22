from rest_framework import serializers
from image.models import Image, Document, Material, Feature, ImageItem


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "name", "image_url", "price",
                  "total_love", "location", "type"]


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"


class ImageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageItem
        fields = "__all__"


class SingleImageSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(read_only=True, many=True)
    items = ImageItemSerializer(Image, read_only=True, many=True)

    class Meta:
        model = Image
        fields = ["id", "name", "image_url", "price",
                  "total_love", "location", "type", "materials_ids", "feature_ids",
                  "related_item", "status", "total_room", "diensions", "garage",
                  "year_build", "type", "total_bed", "location", "description",
                  "total_bathsroom", "documents", "items"]
