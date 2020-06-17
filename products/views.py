from django.shortcuts import render, get_object_or_404
from .models import Product, Category


"""
    def product_details(request, category_slug, product_slug):
         A VIEW FOR AN INDIVIDUAL PRODUCT
        try:
            product = get_object_or_404(category__slug=category_slug, slug=product_slug)

        except Exception as e:
            raise e
        context = {
            'product': product
        }
        return render(request, 'products/product_details.html', context)
"""


def product_details(request, slug):
    """ INDIVIDUAL PRODUCT DETAILS """
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }
    return render(request, 'products/product_details.html', context)
