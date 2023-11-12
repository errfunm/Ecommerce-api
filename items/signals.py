from django.db.models.signals import pre_save, post_save, post_delete
from django.contrib.auth.models import User
from django.core.signals import request_finished
from django.dispatch import receiver
from items.models.cart_item import CartItem
from items.models.shopping_session import ShoppingSession


@receiver(post_save, sender=User)
def create_cart_for_new_user(sender, instance, created, **kwargs):
    if created:
        cart = ShoppingSession.objects.create(user=instance)
        cart.save()


@receiver(post_save, sender=CartItem)
def total_calculation(sender, instance, created, **kwargs):
    created_instance = instance
    price = created_instance.product.price
    quantity = instance.quantity
    total = ShoppingSession.objects.get(id=created_instance.shopping_session.id).total

    if created:
        total_price = quantity * price
        ShoppingSession.objects.filter(
            id__exact=created_instance.shopping_session.id
        ).update(total=total_price)

    total_price = quantity * price
    ShoppingSession.objects.filter(
        id__exact=created_instance.shopping_session.id
    ).update(total=total_price)
