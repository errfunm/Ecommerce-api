from rest_framework import serializers

# models
from items.models.product import Product
from items.models.category import Category
from items.models.brand import Brand
from items.models.cart_item import CartItem
from items.models.shopping_session import ShoppingSession
from items.models.image import Image


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ["url", "id", "name", "description", "price", "category", "brand", "images"]
        read_only_fields = ["images"]


class ShoppingSessionSerializer(serializers.HyperlinkedModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = ShoppingSession
        fields = "__all__"


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    shopping_session = serializers.HyperlinkedRelatedField(
        label="User's cart",
        view_name='shoppingsession-detail',
        read_only=True
    )
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = "__all__"
