from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import permissions, status
from items.api.v1.serializers import ShoppingSessionSerializer
from items.models import ShoppingSession, Product, CartItem


class CustomerCart(ListAPIView):
    serializer_class = ShoppingSessionSerializer
    queryset = ShoppingSession.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])  
def add_to_cart(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except:
        return Response({"detail": "Product with given id not found."}, status=status.HTTP_404_NOT_FOUND)
    
    shopping_session = ShoppingSession.objects.get(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(shopping_session=shopping_session, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    data = {
        "created": created,
        "quantity": cart_item.quantity,
    }
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def remove_from_cart(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(id=cart_item_id)
    except:
        return Response({"detail": "Cart item with given id not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if cart_item.quantity > 1 :
        cart_item.quantity -= 1
        cart_item.save()
        return Response({"deleted": False, "quantity": cart_item.quantity}, status=status.HTTP_200_OK)
    else:
        cart_item.delete()
        return Response({"deleted": True, "quantity": 0}, status=status.HTTP_200_OK)


@api_view(['GET'])
#@permission_classes([permissions.IsAuthenticated])
def cart_total_quantity(request, cart_id):
    cart = ShoppingSession.objects.get(id=cart_id)
    return Response(data={"total_quantity": cart.total_items_quantity}, status=status.HTTP_200_OK)
