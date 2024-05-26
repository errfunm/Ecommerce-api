from django.db import models
from django.contrib.auth.models import User


class ShoppingSession(models.Model):
    user = models.OneToOneField(User, related_name="cart", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def total_price(self):
        """Calculates the total price of all items in the shopping session."""
        total = 0
        for item in self.cart_items.all():
            total += item.quantity * item.product.price
        return total

    @property
    def total_price_with_discount(self):
        """ Calculates the total price with discounts applied."""
        total_with_discount = 0
        for item in self.cart_items.all():
            total_with_discount += item.quantity * item.product.selling_price
        return total_with_discount

    @property
    def total_items_quantity(self):
        """ returns total number of items in the shopping session"""
        quantity_sum = 0
        for item in self.cart_items.all():
            quantity_sum += item.quantity
        return quantity_sum

    def __str__(self):
        username = str(self.user.username)
        return username+"'s cart"
