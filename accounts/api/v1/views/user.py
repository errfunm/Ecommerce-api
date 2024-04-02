from .__init__ import *
from django.contrib.auth.models import User
from accounts.api.v1.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import logout as Logout


class UserViewSet(viewsets.ModelViewSet):

    """
    Django User Model
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        """
        Current user.
        """
        # pk=self.request.user.pk
        # user = User.objects.filter(pk=pk)
        print(request.user.username)
        serializer = self.get_serializer(instance=request.user)
        data = serializer.data
        print(data)
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False)
    def logout(self, request):
        """
        logout the current user.
        """
        Logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
