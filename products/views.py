from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_detail(request, id, slug):
    """ INDIVIDUAL PRODUCT DETAILS """
    product = get_object_or_404(Product,
                                slug=slug,
                                id=id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
