from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from . import views


def product_details(request, category_slug, product_slug):
    """ A VIEW FOR AN INDIVIDUAL PRODUCT """
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'product': product
    }
    return render(request, 'products/product_details.html', context)
