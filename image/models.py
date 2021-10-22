from django.db import models


class Image(models.Model):
    image_url = models.ImageField(upload_to='storage/images/')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    location = models.CharField(max_length=255)
    total_bed = models.IntegerField()
    total_bathsroom = models.IntegerField()
    aria = models.IntegerField()
    price = models.IntegerField()
    total_love = models.IntegerField()
    parent = models.IntegerField()
    type = models.CharField(max_length=255)
    related_item = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    total_room = models.IntegerField()
    diensions = models.CharField(max_length=255)
    garage = models.IntegerField()
    year_build = models.CharField(max_length=255)
    materials_ids = models.CharField(max_length=255)
    feature_ids = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class ImageItem(models.Model):
    image = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name="items")
    image_url = models.ImageField(upload_to='storage/images/')


class Document(models.Model):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name="documents")


class Material(models.Model):
    name = models.CharField(max_length=255)


class Feature(models.Model):
    name = models.CharField(max_length=255)
