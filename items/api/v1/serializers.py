from rest_framework import serializers

# models
from items.models import (
    Product,
    Category,
    Brand,
    CartItem,
    ShoppingSession,
    Image,
    Order,
    OrderItem
)


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
        fields = ["cart_items", "total_price", "total_price_with_discount", "total_items_quantity"]


class OrderItemListSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(source='product', read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(source='order', read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'order_id', 'product_id', 'quantity', 'created_at')


class OrderListSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(source='customer', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer_id', 'payable_price', 'status', 'created_at', 'updated_at')


class OrderDetailSerializer(serializers.ModelSerializer):
    items = OrderItemListSerializer(many=True)
    customer_id = serializers.PrimaryKeyRelatedField(source='customer', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer_id', 'payable_price', 'status', 'created_at', 'updated_at', 'items')
