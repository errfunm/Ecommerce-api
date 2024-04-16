from rest_framework import generics
from rest_framework import permissions
from items.models import ShoppingSession
from items.api.v1.serializers import ShoppingSessionSerializer


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class ShoppingSessionList(generics.ListCreateAPIView):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset


class ShoppingSessionDetail(generics.RetrieveAPIView):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer
    permission_classes = [permissions.DjangoModelPermissions, IsOwner]

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
