from django.shortcuts import render, redirect
from products.models import Product
from .models import OrderItem
from django.contrib import messages


def view_cart(request):
    """ VIEW FOR SHOPPING CART """
    print(request.session)
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
        messages.info(request, "Product added to your bag.")

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
