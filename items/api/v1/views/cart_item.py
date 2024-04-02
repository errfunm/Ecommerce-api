from .__init__ import *
from items.models.cart_item import CartItem
from items.api.v1.serializers import CartItemSerializer
from rest_framework import status


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
            return Response({"message": "Item exists."}, status=status.HTTP_400_BAD_REQUEST)

        else:

            change = serializer.validated_data.get("quantity")
            if change == None:
                change = 1
                
            try:
                CartItem.update_quantity_in_inventory(new_item_product_id, change)

            except:
                return Response(
                    {"Not enough available."}, status=status.HTTP_400_BAD_REQUEST
                )
            else:
                self.create(request, *args, **kwargs)
                return Response({"message": "Cart item updated/created successfully."})

    def get_queryset(self):
        queryset = self.queryset.filter(shopping_session__user=self.request.user)
        return queryset


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        product_id = serializer.validated_data.get("product").id
        change = serializer.validated_data.get("quantity") - instance.quantity
        shopping_session = instance.shopping_session
        try:
            CartItem.update_quantity_in_inventory(product_id, change, shopping_session)
        except:
            return Response(
                {"message": "Not enough available."}, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            self.update(request, *args, **kwargs)
            return Response({"message": "Cart item updated successfully."})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        change = -1 * instance.quantity
        shopping_session = instance.shopping_session
        product_id = instance.product.id
        CartItem.update_quantity_in_inventory(product_id, change)
        return self.destroy(request, *args, **kwargs)
