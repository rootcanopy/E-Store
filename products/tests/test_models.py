from django.test import TestCase
from products.models import Product, Category
from django.urls import reverse


class ProductModelsTest(TestCase):

    def test_string_representation(self):
        product = Product(name='Test Product')
        self.assertEqual(str(product), product.name)

    def test_product_details_view(self):
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'products/product_details.html')


class CategoryModelsTest(TestCase):

    def test_string_representation(self):
        category = Category(name='Books')
        self.assertEqual(str(category), category.name)
