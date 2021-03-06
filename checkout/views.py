from django.shortcuts import (
    render, redirect, reverse, get_object_or_404,
    HttpResponse
)
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages
from .forms import CheckoutForm
from .models import Order, OrderItem
from products.models import Product
from cart.cart_context import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:    
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.' )
        return HttpResponse(content=e, status=400)


# TO DISPLAY THE CHECKOUT FORM
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'address': request.POST['address'],
            'address2': request.POST['address2'],
            'county': request.POST['county'],
        }
        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            order = checkout_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for product_id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=product_id)
                    if isinstance(quantity, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please contact us for assistance!"
                    ))
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save-info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_id]))
        else:
            messages.error(request, 'There was an error with your form. \
                                    Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('home'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    template = 'checkout/checkout.html'
    context = {
        'checkout_form': CheckoutForm(),
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


# HANDLES SUCCESSFUL PAYMENT
def checkout_success(request, order_id):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_id=order_id)
    messages.success(request, f'Order successfully processed! \
                            Your order number is {order_id}. A confirmation \
                            email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
