from .__init__ import *
from items.models.customer import Customer
from items.api.v1.serializers import UserSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by("-date_joined")
    # authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
