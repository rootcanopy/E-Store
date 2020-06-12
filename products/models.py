from django.db import models


class Product(models.Model):
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=1024, blank=True)
    author = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=250, blank=True)
    ratings = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    discount = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
