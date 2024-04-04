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
