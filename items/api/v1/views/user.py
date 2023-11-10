from .__init__ import *
from django.contrib.auth.models import User
from items.api.v1.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    
    """
    Django User Model
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
