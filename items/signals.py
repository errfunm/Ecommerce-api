from django.db.models.signals import post_save, post_delete
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from items.models.cart_item import CartItem
from items.models.shopping_session import ShoppingSession

User = get_user_model()


@receiver(post_save, sender=User)
def create_cart_for_new_user(sender, instance, created, **kwargs):
    if created:
        cart = ShoppingSession.objects.create(user=instance)
        cart.save()


@receiver(post_delete, sender=User)
def delete_cart_for_deleted_user(sender, instance, **kwargs):
    cart = ShoppingSession.objects.filter(user=instance)
    cart.delete()
