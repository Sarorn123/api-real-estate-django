from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Role, User_role, AccessModule, TitleUI
from .serializers import RoleSerializer, UserRoleSerializer, AccessModuleSerializer, TitleUISerializer

# username = rorn, password = rorn123456


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        role = User_role.objects.get(user_id=user.id)
        serializer = UserRoleSerializer(role, many=False)
        data = serializer.data
        role_id = data['role_id']

        roleData = Role.objects.get(id=role_id)
        role_serializer = RoleSerializer(roleData, many=False)

        if role_id == 1:
            menu_tree = "superAdmin tree"
        elif role_id == 2:
            access = AccessModule.objects.filter(user_type="ADMIN")
            serializer = AccessModuleSerializer(access, many=True)
            menu_tree = serializer.data
        elif role_id == 3:
            access = AccessModule.objects.filter(user_type="USER")
            serializer = AccessModuleSerializer(access, many=True)
            menu_tree = serializer.data

        data = {
            'token': token.key,
            'user_id': user.id,
            'user_name': user.username,
            'email': user.email,
            'role_data': role_serializer.data,
            'menu_tree': menu_tree,
        }

        return Response({"data": data})


@api_view(['GET'])
def getAllUsers(request):
    return Response("hello")
