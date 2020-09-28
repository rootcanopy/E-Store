from django.test import Client, TestCase
from django.urls import reverse

from products.models import Product, Category


class ProductTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Spinach',
            category='food',
            price='10.00',
        )
    
    def test_product_listing_home(self):
        self.assertEqual(f'{self.product.name}', 'Spinach')
        self.assertEqual(f'{self.product.category}', 'food')
        self.assertEqual(f'{self.product.price}', '10.00')
    
    def test_product_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Spinach')
        self.assertTemplateUsed(response, 'home/index.html')

