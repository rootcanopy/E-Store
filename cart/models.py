from django.db import models
from products.models import Product


# MODEL FOR THE ORDER/CART OBJECT ITEM
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # order = models.ForeignKey(Order, null=False, blank=False,
    #                          on_delete=models.CASCADE, related_name='lineitems')
    quantity = models.IntegerField(default=1)
