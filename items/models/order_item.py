from django.db import models
from . import Order, Product


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items",)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name="order_items",)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.order} - {self.product}"
