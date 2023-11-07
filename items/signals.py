from django.db.models.signals import pre_save, post_save, post_delete
from django.core.signals import request_finished
from django.dispatch import receiver
from items.models.customer import Customer
from items.models.cart_item import CartItem
from items.models.shopping_session import ShoppingSession


@receiver(post_save, sender=Customer)
def create_cart_for_new_user(sender, instance, created, **kwargs):
    if created:
        cart = ShoppingSession.objects.create(user=instance)
        cart.save()


@receiver(post_save, sender=CartItem)
def add_to_total(sender, instance, created, **kwargs):
    if created:
        just_created_cart_item = instance
        price = just_created_cart_item.product.price
        quantity = instance.quantity
        total = ShoppingSession.objects.get(
            id=just_created_cart_item.shopping_session.id
        ).total
        total_price = (quantity * price) + total
        ShoppingSession.objects.filter(
            id__exact=just_created_cart_item.shopping_session.id
        ).update(total=total_price)


@receiver(post_delete, sender=CartItem)
def sub_from_total(sender, instance, **kwargs):
    just_deleted_cart_item = instance
    price = just_deleted_cart_item.product.price
    quantity = instance.quantity
    total = ShoppingSession.objects.get(
        id=just_deleted_cart_item.shopping_session.id
    ).total
    total_price = total - (quantity * price)
    ShoppingSession.objects.filter(
        id__exact=just_deleted_cart_item.shopping_session.id
    ).update(total=total_price)
