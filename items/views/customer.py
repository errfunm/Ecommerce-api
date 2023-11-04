from .__init__ import *


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by("-date_joined")
    # authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
