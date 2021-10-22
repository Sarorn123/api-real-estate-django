from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role, User_role, AccessModule, TitleUI


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_role
        fields = "__all__"

class AccessModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessModule
        fields = "__all__"

class TitleUISerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleUI
        fields = "__all__"