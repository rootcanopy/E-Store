from django.shortcuts import (
    render, redirect, reverse
)
from django.conf import settings
from django.contrib import messages
from .forms import CheckoutForm
from cart.cart_context import cart_contents

import stripe

# TO DISPLAY THE CHECKOUT FORM
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty')
        return redirect(reverse('checkout'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    checkout_form = CheckoutForm()

    print(intent)

    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)
