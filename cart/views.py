from django.shortcuts import render
from products.models import Product


def view_cart(request):
    """ VIEW FOR SHOPPING CART """
    print(request.session)
    return render(request, 'cart/shopping_cart.html')


"""
    def add_to_bag(request, slug):
        product = get_object_or_404(Product, slug=slug)
"""
