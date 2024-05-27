from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# views
from items.api.v1.views import *

urlpatterns = [
    path("api_schema/", SpectacularAPIView.as_view(), name="api_schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="api_schema")),
    path("category/", CategoryList.as_view(), name="category-list"),
    path("category/<int:pk>", CategoryDetail.as_view(), name="category-detail"),
    path("image/", ImageList.as_view(), name="image-list"),
    path("image/<int:pk>", ImageDetail.as_view(), name="image-detail"),
    path("brand/", BrandList.as_view(), name="brand-list"),
    path("brand/<int:pk>", BrandDetail.as_view(), name="brand-detail"),
    path("products/", ProductList.as_view(), name="product-list"),
    path("products/<int:pk>", ProductDetail.as_view(), name="product-detail"),
    path("shopping_session/", ShoppingSessionList.as_view(), name="shopping-session-list"),
    path(
        "shopping_session/<int:pk>", ShoppingSessionDetail.as_view(), name="shoppingsession-detail"
    ),
    path("cart_item/", CartItemList.as_view(), name="cart-item-list"),
    path(
        "cart_item/<int:pk>", CartItemDetail.as_view(), name="cartitem-detail"
    ),

    path('cart/', CustomerCart.as_view(), name="customer-cart"),
    path('cart/add/<int:product_id>', add_to_cart, name="add-to-cart"),
    path('cart/remove/<int:cart_item_id>', remove_from_cart, name="remove-from-cart"),
    path('cart/total_quantity', cart_total_quantity, name="cart-total-quantity"),

    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/<int:pk>", OrderDetailView.as_view(), name="order-detail"),
    path('orders/create/', create_order, name="order-create"),
    path('orders/payment/verify', payment_verify, name='payment-verify')
]
