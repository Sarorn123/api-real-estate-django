from django.contrib import admin
from django.urls import path, include
from systemUser.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/auth/', CustomAuthToken.as_view()),
    path('api/', include('systemUser.urls')),
    path('api/', include('image.urls')),

]
