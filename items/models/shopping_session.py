from .__init__ import *
from customer import *


class ShoppingSession(models.Model):
    user = models.OneToOneField(Customer, related_name="cart", on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.user.username
