from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.urlpatterns import format_suffix_patterns

# views
from .views.brand import BrandList, BrandDetail
from .views.cart_item import CartItemList, CartItemDestroy
from .views.category import CategoryList, CategoryDetail
from .views.user import UserViewSet
from .views.group import GroupViewSet
from .views.image import ImageList, ImageDetail
from .views.product import ProductList, ProductDetail
from .views.shopping_session import ShoppingSessionList, ShoppingSessionDetail


router = DefaultRouter()
router.register(r"User", UserViewSet, basename="customer")
router.register(r"groups", GroupViewSet, basename="group")

urlpatterns = [
    # path("", api_root, name="api-root"),
    path("api_schema/", SpectacularAPIView.as_view(), name="api_schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="api_schema")),
    path("category/", CategoryList.as_view(), name="category-list"),
    path("category/<int:pk>", CategoryDetail.as_view(), name="category-detail"),
    path("image/", ImageList.as_view(), name="image-list"),
    path("image/<int:pk>", ImageDetail.as_view(), name="image-detail"),
    path("brand/", BrandList.as_view(), name="brand-list"),
    path("brand/<int:pk>", BrandDetail.as_view(), name="brand-detail"),
    path("products/", ProductList.as_view(), name="product-list"),
    path("poducts/<int:pk>", ProductDetail.as_view(), name="product-detail"),
    path("cart/", ShoppingSessionList.as_view(), name="shopping-session-list"),
    path(
        "cart/<int:pk>", ShoppingSessionDetail.as_view(), name="shoppingsession-detail"
    ),
    path("cart_item/", CartItemList.as_view(), name="cart-item-list"),
    path("cart_item/<int:pk>", CartItemList.as_view(), name="cartitem-detail"),
    path(
        "cart_item/delete/<int:pk>", CartItemDestroy.as_view(), name="cart-item-delete"
    ),
    path("", include(router.urls)),
]
