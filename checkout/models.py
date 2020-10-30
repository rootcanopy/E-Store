import uuid
from django.db.models import Sum
from django.conf import settings
from django.db import models

from django_countries.fields import CountryField
from products.models import Product

from profiles.models import UserProfile


# MODEL FOR THE ORDER OBJECT
class Order(models.Model):
    order_id = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    address = models.CharField(max_length=80, null=False, blank=False)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_id(self):
        # GENERATES ORDER NUMBER
        return uuid.uuid4().hex.upper()
    
    def update_order_total(self):
        # UPDATE GRAND TOTAL E/ TIME ORDERITEM IS ADDED
        self.order_total = self.orderitems.aggregate(Sum('orderitem_total'))['orderitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        # OVERRIDE ORIG SAVE METHOD TO SET ORDER ID
        # IF ! BEEN SET ALREADY
        if not self.order_id:
            self.order_id = self._generate_order_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id


# MODEL FOR THE OBJECT ITEM
class OrderItem(models.Model):
    order = models.ForeignKey(Order, default=True, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    orderitem_total = models.DecimalField(max_digits=6, null=False, default=True, decimal_places=2)

    def save(self, *args, **kwargs):
        # OVERRIDE ORIGINAL SAVE METHOD && SET THE ORDERITEM TOTAL
        # && UPDATE THE ORDER TOTAL
        self.orderitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ID {self.product.id} on order {self.order.order_id}'
