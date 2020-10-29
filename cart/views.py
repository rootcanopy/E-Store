from django.shortcuts import (
    render, redirect, reverse, get_object_or_404,
    HttpResponse
)
from products.models import Product

from django.contrib import messages


# VIEW THE CART
def view_cart(request):
    """ VIEW FOR SHOPPING CART """
    return render(request, 'cart/cart.html')


# ADD TO THE CART
def add_to_cart(request, product_id):
    """ ADD A PRODUCT AND QTY TO THE CART """
    product = Product.objects.get(id=product_id)
    quantity = int(request.POST.get('quantity')) # this needs attn
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')
                                    
    else:
        cart[product_id] = quantity
        messages.info(request, f'{product.name} Added to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)


# UPDATE THE CART VIEW
def update_cart(request, product_id):
    """ ADJUST QTY IN CART """
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[product_id] = quantity
        messages.success(request,
                            (f'Updated {product.name} quantity to {cart[product_id]}'))
    else:
        cart.pop(product_id)
        messages.success(request,            
                            (f'Removed {product.name} '
                            f'from your bag'))

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


# REMOVE FROM THE CART
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    cart.pop(product_id)
    messages.success(request, f'Removed {product.name} from your cart')
    request.session['cart'] = cart
    return HttpResponse(status=200)
