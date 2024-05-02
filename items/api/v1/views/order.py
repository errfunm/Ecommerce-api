import zibal.zibal as zibal
from django.db import transaction
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from ..serializers import OrderListSerializer, OrderDetailSerializer
from items.models import Order, OrderItem


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user


class OrderListView(ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(customer=self.request.user)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def create_order(request):
    customer = request.user
    cart = customer.cart

    with transaction.atomic():
        order = Order(customer=customer, payable_price=cart.total_price_with_discount, status="Pending")
        order.save()

        for item in cart.cart_items.all():
            product = item.product
            order_item = OrderItem(order=order, product=product,
                                   quantity=item.quantity)  # copy cart items into order items
            order_item.save()
            try:
                product_inventory = product.inventory
                product_inventory.quantity -= item.quantity
                product_inventory.save()
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            # connect to payment gateway 'zibal'
            payable_price_in_rial = order.payable_price * 10
            merchant_id = 'zibal'
            callback_url = 'http://localhost:8000/api/v1/orders/payment/verify'
            zb = zibal.zibal(merchant_id, callback_url)
            request_to_zibal = zb.request(amount=payable_price_in_rial, order_id=order.id)

    serializer = OrderDetailSerializer(order)
    return Response({"order": serializer.data, "zibal": request_to_zibal}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def payment_verify(request):
    callback_url = 'http://localhost:8000/api/v1/orders/payment/verify'
    zb = zibal.zibal('zibal', callback_url)
    verify_zibal = zb.verify(trackId=request.GET['trackId'])
    result_code = verify_zibal['result']

    data = {
        "result_code": result_code,
        "detail": zb.verify_result(result_code),
    }

    if result_code in [100, 202]:
        order = Order.objects.get(id=request.GET['orderId'])
        success = bool()
        if result_code == 100 and verify_zibal['status'] == 1:
            success = True
        elif result_code == 202:
            success = False
        finalize_payment(order=order, success=success)
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


def finalize_payment(order, success):
    if success:
        order.status = "Shipped"
        order.save()
        # clear customer's cart
        for item in order.customer.cart.cart_items.all():
            item.delete()
    else:
        order.status = "Cancelled"
        order.save()
        # roll back product stock
        for item in order.items.all():
            product_inventory = item.product.inventory
            product_inventory.quantity += item.quantity
            product_inventory.save()


class OrderDetailView(RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    permission_classes = [IsOwner]
