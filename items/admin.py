from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from items.models.product import Product
from items.models.category import Category
from items.models.brand import Brand
from items.models.cart_item import CartItem
from items.models.shopping_session import ShoppingSession

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CartItem)
admin.site.register(ShoppingSession)
