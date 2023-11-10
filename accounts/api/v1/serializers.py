from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    shopping_session = serializers.HyperlinkedRelatedField(
        view_name="shopping_session-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["id", "username", "shopping_session"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
