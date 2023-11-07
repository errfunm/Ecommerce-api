from django.contrib.auth.models import Group
from items.models.customer import Customer
from rest_framework import serializers

# models
from items.models.product import Product
from items.models.category import Category
from items.models.brand import Brand
from items.models.cart_item import CartItem
from items.models.shopping_session import ShoppingSession
from items.models.customer import Customer
from items.models.image import Image


class UserSerializer(serializers.HyperlinkedModelSerializer):
    shopping_session = serializers.HyperlinkedRelatedField(
        view_name="shopping_session-detail", read_only=True
    )

    class Meta:
        model = Customer
        fields = ["shopping_session", "uuid"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


"""class ProductInventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductInventory
        fields = "__all__"""


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ShoppingSessionSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.HyperlinkedRelatedField(User, )
    total = serializers.ReadOnlyField()

    class Meta:
        model = ShoppingSession
        fields = "__all__"


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"
