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
        fields = ["url", "id", "name", "description", "price", "selling_price",
                  "discount_percent", "category", "brand", "images"]
        read_only_fields = ["images"]


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = CartItem
        fields = ["url", "id", "shopping_session", "product", "product_id", "quantity"]
        read_only_fields = ["shopping_session", "product"]


class ShoppingSessionSerializer(serializers.HyperlinkedModelSerializer):
    cart_items = CartItemSerializer(many=True)
    
    class Meta:
        model = ShoppingSession
        fields = ["cart_items", "total_price", "total_price_with_discount"]
