from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.user import UserViewSet
from .views.group import GroupViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"User", UserViewSet, basename="user")
router.register(r"groups", GroupViewSet, basename="group")

urlpatterns = [
    path("token-auth", obtain_auth_token),
    path("", include(router.urls)),
]
