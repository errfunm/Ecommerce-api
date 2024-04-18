from django.contrib.auth.models import Group, User, Permission
from rest_framework import serializers


class UserListSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "cart", "email", "first_name", "last_name", "password"]
        read_only_fields = ["cart"]


class RegisterCustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        # Creates new user and adds it to group 'customer'
        customer_grp = Group.objects.get(name="customer")
        customer = User(username=validated_data['username'])
        customer.set_password(validated_data['password'])
        customer.save()
        customer.groups.add(customer_grp)
        return customer


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "cart", "first_name", "last_name", "email"]
        read_only_fields = ["cart", "username"]


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = "__all__"
