from django.contrib import admin
from items.models import Product
from items.models import Category
from items.models import Brand
from items.models import CartItem
from items.models import ShoppingSession
from items.models import ProductInventory
from items.models import Image


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CartItem)
admin.site.register(ShoppingSession)
admin.site.register(ProductInventory)
admin.site.register(Image)