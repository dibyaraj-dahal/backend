from django.test import TestCase
from . utils import add
from django.urls import reverse

# Create your tests here.


class AddFunctionTestCase(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)


class RegistrationFromPageTestCase(TestCase):
    def test_registration_contains_input_text(self):
        response = self.client.get(reverse('registration:form'))
        self.assertContains(response.status_code, 200)
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Email')
        self.assertContains(response, "Password:")
