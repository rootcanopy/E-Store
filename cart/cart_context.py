from django.conf import settings
from decimal import Decimal
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    product = None

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        free_delivery_allowance = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_allowance = 0

    grand_total = delivery + total

    # if product.discount > 0:
    #    discount = product.price - product.discount * Decimal

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_allowance': free_delivery_allowance,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
