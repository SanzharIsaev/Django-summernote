from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CatalogAPIView 

router = DefaultRouter()
router.register(r'catalogs', CatalogAPIView)


urlpatterns = [
    path('', include(router.urls)),
]