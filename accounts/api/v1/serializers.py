from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserListSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "cart", "email", "first_name", "last_name", "password"]
        read_only_fields = ["cart"]
        write_only_fields = ["password"]


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "cart", "first_name", "last_name", "email"]
        read_only_fields = ["cart", "username"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
