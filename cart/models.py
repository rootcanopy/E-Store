from django.db import models
from products.models import Product


# MODEL FOR THE ORDER/CART OBJECT ITEM
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_total = models.DecimalField(max_digits=6, null=False, default=True, decimal_places=2)

    def __str__(self):
        return str(self.pk)
