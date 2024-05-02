from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from items.models.shopping_session import ShoppingSession

User = get_user_model()


@receiver(post_save, sender=User)
def create_cart_for_new_user(sender, instance, created, **kwargs):
    if created:
        cart = ShoppingSession.objects.create(user=instance)
        cart.save()

