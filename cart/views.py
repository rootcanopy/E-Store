from django.shortcuts import (
    render, redirect, reverse, get_object_or_404,
    HttpResponse
)
from products.models import Product
from .models import OrderItem
from django.contrib import messages


def view_cart(request):
    """ VIEW FOR SHOPPING CART """
    return render(request, 'cart/shopping_cart.html')


def add_to_cart(request, product_id):
    """ ADD A PRODUCT AND OR QTY TO THE CART """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
        messages.info(request, 'Product quantity updated')
    else:
        cart[product_id] = quantity
        messages.info(request, "Product added to your cart.")

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, product_id):
    """ ADJUST QTY IN CART """
    quantity = int(request.POST.get('quantity'))
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[product_id] - quantity
    else:
        cart.pop(product_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, product_id):
    """ VIEW TO REMOVE A PRODUCT FROM CART """
    try:
        cart = request.session.get('cart', {})

        cart.pop(product_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
