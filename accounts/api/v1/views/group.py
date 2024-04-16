from rest_framework import permissions
from rest_framework import viewsets
from django.contrib.auth.models import Group
from accounts.api.v1.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
