from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from checkout.models import OrderItem
from products.models import Product
from django import template


def cart_contents(request):

    order_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for product_id, quantity in cart.items():
        if isinstance(quantity, int):
            product = get_object_or_404(Product, id=product_id)
            total += quantity * product.price
            product_count += quantity
            order_items.append({
                'product_id': product_id,
                'quantity': quantity,
                'product': product,
            })


    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    # if product.discount > 0:
    #    discount = product.price - product.discount * Decimal

    context = {
        'order_items': order_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
