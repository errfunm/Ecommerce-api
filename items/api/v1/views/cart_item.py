from .__init__ import *
from items.models.cart_item import CartItem
from items.api.v1.serializers import CartItemSerializer

class CartItemList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_item_cart_id = serializer.validated_data.get("shopping_session").id
        new_item_product_id = serializer.validated_data.get("product").id
        match_item = CartItem.objects.filter(
            shopping_session_id=new_item_cart_id, product_id__exact=new_item_product_id
        ).first()
        if match_item:
            match_item.quantity += serializer.validated_data.get("quantity")
            match_item.save()
        else:
            return self.create(request, *args, **kwargs)
        return Response({"message": "Cart item updated/created successfully."})

    def get_queryset(self):
        queryset = self.queryset.filter(shopping_session__user=self.request.user)
        return queryset


class CartItemDestroy(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def delete(self, request, *args, **kwargs):
        cart_item = self.get_object()
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            return self.destroy(request, *args, **kwargs)
        return Response({"message": "Cart item updated/deleted successfully."})
