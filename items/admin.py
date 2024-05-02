from django.contrib import admin
from items.models import Product
from items.models import Category
from items.models import Brand
from items.models import CartItem
from items.models import ShoppingSession
from items.models import ProductInventory
from items.models import Image
from items.models import Discount
from items.models import Order, OrderItem

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CartItem)
admin.site.register(ShoppingSession)
admin.site.register(ProductInventory)
admin.site.register(Image)
admin.site.register(Discount)
admin.site.register(Order)
admin.site.register(OrderItem)
