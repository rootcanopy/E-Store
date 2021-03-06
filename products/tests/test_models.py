from django.test import TestCase
from products.models import Product, Category
from django.urls import reverse


class ProductModelTest(TestCase):

    def test_verbose_name_plural(self):
        self.assertEqual(str(Product._meta.verbose_name_plural), 'products')

    def test_string_representation(self):
        product = Product(name='Test Product')
        self.assertEqual(str(product), product.name)

    def test_product_details_view(self):
        response = self.client.get(self.products.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'product_details.html')

    def test_get_absolute_url(self):
        product = Product.objects.get(id=1)
        self.assertEquals(product.get_absolute_url(), '/products/pinebook-pro/1')


class CategoryModelTest(TestCase):

    def test_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural), 'categories')

    def test_get_absolute_url(self):
        return reverse('products_by_category', kwargs={self.slug})

    def test_string_representation(self):
        category = Category(name='Books')
        self.assertEqual(str(category), category.name)
