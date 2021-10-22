from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Role, User_role, AccessModule, TitleUI
from .serializers import RoleSerializer, UserRoleSerializer, AccessModuleSerializer,TitleUISerializer

from image.functions import getDiscoverData, getPropertyData, getExploreData, getBackgroundImage
from agency.functions import getAllAgencyEmployees, getAllAgencys


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        role = User_role.objects.get(user_id = user.id)
        serializer = UserRoleSerializer(role, many=False)
        data = serializer.data
        role_id = data['role_id']

        roleData = Role.objects.get(id=role_id)
        role_serializer = RoleSerializer(roleData, many=False)

        if role_id == 1:
            menu_tree = "superAdmin tree"
            uiData = []
            uiData2 = []
        elif role_id == 2:
            menu_tree = "admin tree"
            uiData = []
            uiData2 = []
        elif role_id == 3:
            menu_tree = "client" 
            uiData = []
            uiData2 = []
        else:
            access = AccessModule.objects.all()
            serializer = AccessModuleSerializer(access,many=True)
            menu_tree = serializer.data

            ui = TitleUI.objects.get(id=1)
            ui2 = TitleUI.objects.get(id = 2) 
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
            'token': token.key,
            'user_id': user.id,
            'user_name': user.username,
            'email': user.email,
            'role_data': role_serializer.data,
            'menu_tree' : menu_tree,
            'title_1' : uiData,
            'title_2' : uiData2,
            'background_image' : bg_image['image_url'],
            'discover_data' : discover,
            'explore_property' : property,
            'explore_property_city' : explore,
            'recommend_agency' : agency,
            "feature_agency" : employee,
        }

        return Response({"data" : data})

@api_view(['GET'])
def getAllUsers(request):
    return Response("hello")

