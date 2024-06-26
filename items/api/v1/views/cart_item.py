from rest_framework import generics
from rest_framework.response import Response
from items.models import CartItem
from items.api.v1.serializers import CartItemSerializer
from rest_framework import status, permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.shopping_session.user == request.user


class CartItemList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Check if the item already exists in the cart
        if CartItem.objects.filter(
            shopping_session=request.user.cart,
            product=serializer.validated_data["product"]
        ).exists():
            return Response({"error": "item exists"}, status.HTTP_400_BAD_REQUEST)

        # create the cart item
        self.perform_create(serializer)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(shopping_session=self.request.user.cart)

    def get_queryset(self):
        queryset = self.queryset.filter(shopping_session__user=self.request.user)
        return queryset


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsOwner]

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        self.update(request, *args, **kwargs)

        return Response(serializer.data['quantity'], status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)
