from django.db import models
from .shopping_session import *
from .product import *
from .product_inventory import ProductInventory
from django.db import transaction
from django.core.validators import MinValueValidator


class CartItem(models.Model):
    shopping_session = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE, verbose_name="user's cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        product_name = self.product.name
        user_name = self.shopping_session.user.username
        return f"{product_name}-{user_name}"


    def save(self, *args, **kwargs):
        pass

    
    def update_quantity_in_inventory(product_id, change, shop_s=None):
        with transaction.atomic():
            product = Product.objects.get(id=product_id)
            # Update CartItem quantity
            if shop_s:
                cart_item = CartItem.objects.get(
                    shopping_session=shop_s, product=product
                )
                cart_item.quantity += change
                if cart_item.quantity == 0:
                    cart_item.delete()

            # Update ProductInventory
            inventory = ProductInventory.objects.get(product=product)
            inventory.quantity -= change
            print("this is the number:", inventory.quantity)
            if inventory.quantity < 0:
                raise "error"

            inventory.save()
