from django.test import Client, TestCase
from django.urls import reverse


class ProductDetailTest(TestCase):

    def test_product_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get('/product/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'PineBookPro')
        self.assertTemplateUsed(response, 'products/product_details.html')
