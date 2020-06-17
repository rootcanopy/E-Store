from django.shortcuts import render
from products.models import Product


def view_cart(request):
    """ VIEW FOR SHOPPING CART """
    return render(request, 'cart/shopping_cart.html')


def add_to_bag(request, slug):
    pass
