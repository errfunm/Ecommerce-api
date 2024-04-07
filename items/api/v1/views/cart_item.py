from .__init__ import *
from items.models import CartItem
from items.api.v1.serializers import CartItemSerializer
from rest_framework import status
from django.core.exceptions import ValidationError


class CartItemList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["shopping_session"] = request.user.cart
        try:
            self.perform_create(serializer)
        except ValidationError:
            return Response({"message": "item exists"})

        return Response({"message": "Cart item updated/created successfully."})

    def perform_create(self, serializer):
        serializer.save(shopping_session=self.request.user.cart)

    def get_queryset(self):
        queryset = self.queryset.filter(shopping_session__user=self.request.user)
        return queryset


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        self.update(request, *args, **kwargs)
        return Response({"message": "Cart item updated successfully."})

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response({"message": "Cart item deleted successfully"})
