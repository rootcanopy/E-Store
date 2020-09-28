from django.test import (
    SimpleTestCase, TestCase, Client
)
from django.urls import reverse


class HomepageTests(TestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')


class Home_PageTest(TestCase):

    def test_home_page_product_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/')
        self.assertTemplateUsed(response, 'home/index.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '')
    
    def test_homepage_doesnt_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be here :)'
        )
