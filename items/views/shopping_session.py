from .__init__ import *
from models.shopping_session import ShoppingSession


class ShoppingSessionList(generics.ListCreateAPIView):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer


class ShoppingSessionDetail(generics.RetrieveAPIView):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer
