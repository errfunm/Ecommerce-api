from django.db import models
from .category import Category
from .brand import Brand
from .discount import Discount


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    discounts = models.ManyToManyField(Discount, related_name="products",)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def selling_price(self):
        discounts = self.discounts.all()
        price = self.price
        for discount in discounts:
            price = price - (self.price * discount.value)
        return price

    @property
    def discount_percent(self):
        price = self.price
        selling_price = self.selling_price
        total_discount_percentage = 100 - ((selling_price / price) * 100)
        return int(total_discount_percentage)

    def __str__(self):
        return self.name
