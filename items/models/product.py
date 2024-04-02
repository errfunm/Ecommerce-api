from django.db import models
from .category import Category
from .brand import Brand


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
