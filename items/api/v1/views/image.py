from .__init__ import *
from items.models import Image
from items.api.v1.serializers import ImageSerializer


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
