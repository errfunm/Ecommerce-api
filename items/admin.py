from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CartItem)
admin.site.register(ShoppingSession)
admin.site.register(Customer)