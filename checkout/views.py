from django.shortcuts import (
    render, redirect, reverse
)
from django.contrib import messages
from .forms import CheckoutForm


# TO DISPLAY THE CHECKOUT FORM
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty')
        return redirect(reverse('checkout'))
    
    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': 'pk_test_C9HJQ1QFL2S9E9LgiOW3oXDq00PPJmu2U5',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)
