from django.db import models
from .shopping_session import ShoppingSession
from .product import Product
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

    class Meta:
        unique_together = [['shopping_session', 'product']]
