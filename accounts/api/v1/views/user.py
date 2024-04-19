from django.contrib.auth.models import User
from django.contrib.auth import logout as Logout
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.api.v1.serializers import UserListSerializer, UserDetailSerializer, RegisterCustomerSerializer


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
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [IsOwner]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ["list", "create"]:
            serializer_class = UserListSerializer
        elif self.action == "register":
            serializer_class = RegisterCustomerSerializer
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

    @action(methods=["POST"], detail=False, permission_classes=[permissions.AllowAny])
    def register(self, request):
        """
        Customer registration endpoint
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {
            "token": {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            },
            "user": serializer.data
        }
        return Response(data=data, status=status.HTTP_201_CREATED)
 