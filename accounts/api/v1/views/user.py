from .__init__ import *
from django.contrib.auth.models import User
from accounts.api.v1.serializers import UserListSerializer, UserDetailSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import logout as Logout


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class UserViewSet(viewsets.ModelViewSet):

    """
    Django User Model
    """

    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [permissions.IsAdminUser]
        elif self.action == "create":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsOwner]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ["list", "create"]:
            serializer_class = UserListSerializer
        else:
            serializer_class = UserDetailSerializer
        return serializer_class

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        """
        Current user.
        """
        serializer = self.get_serializer(instance=request.user)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False)
    def logout(self, request):
        """
        logout the current user.
        """
        Logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

