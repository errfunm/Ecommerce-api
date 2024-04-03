from .__init__ import *
from items.models import ShoppingSession
from items.api.v1.serializers import ShoppingSessionSerializer

class ShoppingSessionList(generics.ListCreateAPIView):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer


class ShoppingSessionDetail(generics.RetrieveAPIView):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer
