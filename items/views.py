from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets

from rest_framework import generics
from rest_framework.reverse import reverse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

# from rest_framework_simplejwt import A
from .permissions import IsCostumer
from .serializers import *
import markdown
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, get_user
from django.conf import settings
from datetime import datetime, timedelta


@api_view(["GET"])
def api_root(request, format=None):
    sessions = request.session

    return Response(
        {
            "users": reverse("api-root", request=request, format=format),
            "product": reverse("product-list", request=request, format=format),
        }
    )


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by("-date_joined")
    # authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShoppingSessionList(generics.ListCreateAPIView):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer


class ShoppingSessionDetail(generics.RetrieveAPIView):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer


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
