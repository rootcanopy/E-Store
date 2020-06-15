from django.db import models
from django.urls import reverse


class Product(models.Model):
    category = models.ForeignKey(
        'Category', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=1024, blank=True)
    author = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=2000, blank=True)
    ratings = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    discount = models.IntegerField(blank=True, null=True)
    in_stock = models.BooleanField(default=True, null=False)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'products'
        index_together = (('id', 'slug'),)

    # def get_absolute_url(self):
    #    return reverse('products:product_details', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name
