from django.shortcuts import (
    render, redirect, reverse
)
from django.contrib import messages
from .forms import CheckoutForm


# TO DISPLAY THE CHECKOUT FORM
def checkout(request):
    cart = request.session.get('cart', {})
    #if not cart:
    #    messages.error(request, 'Your cart is empty')
     #   return redirect(reverse('checkout'))
    
    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
    }
    return render(request, template, context)
