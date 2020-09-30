from decimal import Decimal

from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory

from cart.models import OrderItem
from products.models import Product


class CartInitializeTestCase(TestCase):
    # Test cart initialization
    # Possible outcomes:
    # - cart is an empty dictionary (with input: session that contains no cart)
    # - cart contains is equal to the cart in the session

    def setUp(self):
        self.request = RequestFactory().get('/')

        # ADD THE SESSION
        middleware = SessionMiddleware()
        middleware.process_request(self.request)
        self.request.session.save()

    def test_initialize_cart_clean_session(self):
        # The cart is initialized with a session that contains no cart.
        # In the end it should have a variable cart which is an empty dict.

        request = self.request
        cart = request.session.GET('cart', {})
        self.assertEqual(cart.cart, {})
"""
    def test_initialize_cart_filled_session(self):
        # The cart is initialized with a session that contains a cart.
        # In the end it should have a variable cart which equal to the cart that
        # is in the initial session.

        existing_cart = {
            '1': {
                'name': 'first name',
                'price': '1.01',
                  },
            '2': {
                'name': 'second name',
                'price': '34.1',
            }
        }
        request = self.request
        request.session['cart'] = existing_cart
        cart = request.session.GET('cart', {})
        self.assertEqual(cart.cart, existing_cart)
"""