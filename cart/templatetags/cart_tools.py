from django import template


register = template.Library()


# TO CALCULATE ORDER_ITEM PRICE
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
