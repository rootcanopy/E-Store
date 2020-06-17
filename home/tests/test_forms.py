from django.test import TestCase
from django.core import mail
from django.shortcuts import reverse
from home import forms


class ContactFormTests(TestCase):

    def test_contact_form_sends_email(self):
        form = forms.ContactForm({
            'name': 'Davie B',
            'subject': 'Howiya doin',
            'email': 'dave.trees@gmail.com',
            'message': 'Its been a long time coming',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_contact_us_form(self):
        form = forms.ContactForm({
            'message': "Hi there"})
        self.assertFalse(form.is_valid())

    def test_contact_us_page_works(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')
        self.assertContains(response, 'home')  # TODO
        self.assertIsInstance(
            response.context["form"], forms.ContactForm
        )
