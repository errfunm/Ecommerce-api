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
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = CartItem
        fields = ["url", "id", "shopping_session", "product", "product_id", "quantity"]
        read_only_fields = ["shopping_session", "product"]
