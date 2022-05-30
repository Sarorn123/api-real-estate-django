from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Role(models.Model):
    name = models.CharField(max_length=255)

class User_role(models.Model):
    user_id = models.BigIntegerField(null=True, blank=True)
    role_id = models.BigIntegerField(blank=True, null=True)

class AccessModule(models.Model):
    name = models.CharField(max_length=255)
    parent = models.IntegerField(default=0)
    url = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255, default="USER")
    sortkey = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

class TitleUI(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
