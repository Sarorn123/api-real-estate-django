from django.urls import path, include
from .views import ImageViewSet,DocumentViewSet
from rest_framework.routers import DefaultRouter
from .views import getHouse

router = DefaultRouter()
router.register('house', ImageViewSet, base_name="house")
router.register('document', DocumentViewSet, base_name="document")

urlpatterns = [
    path('image/', include(router.urls)),
    path('image/getHouse/<int:pk>/', getHouse),
]
