from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderItem
from products.models import Product
from profiles.models import UserProfile

import time
import json


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
    # Handle generic/unknown/unexpected webhook event
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_succeeded(self, event):
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
