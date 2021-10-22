from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='storage/images/agencyCompany/')
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)

class AgencyEmployee(models.Model):
    agency = models.ForeignKey(Agency, related_name="employees", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    says = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='storage/images/agencyCompany/')