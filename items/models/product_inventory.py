from django.db import models
from .product import Product
from items.exceptions import OutOfStock


class ProductInventory(models.Model):
    product = models.OneToOneField(
        Product,
        related_name="inventory",
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "product inventories"

    def __str__(self) -> str:
        return f"{self.product} x {self.quantity}"

    def save(self, **kwargs):
        if self.quantity < 0:
            raise OutOfStock(
                f"Not enough items in stock for product: {self.product}"
            )
        return super().save()
