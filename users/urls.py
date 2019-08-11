from .views import (
    edit,
    UserViewSet
)
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('edit/', edit),
]