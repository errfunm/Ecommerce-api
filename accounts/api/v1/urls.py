from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"User", UserViewSet, basename="user")
router.register(r"groups", GroupViewSet, basename="group")

urlpatterns = [
    path("", include(router.urls)),
]
