from rest_framework import generics
from rest_framework import permissions

from items.models import Brand
from items.api.v1.serializers import BrandSerializer


class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
