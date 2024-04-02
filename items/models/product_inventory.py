from django.db import models
from .product import *


class ProductInventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "product inventories"

    def __str__(self) -> str:
        product_name = self.product.name
        return product_name
