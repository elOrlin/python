from unittest.mock import patch
from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
#from core import models

def create_user(email='user@example.com', password='testpass123'):
    "Create and return a new user"
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'orlindiaz@outlook.com'
        password = 'girls754'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'girls754')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
       with self.assertRaises(ValueError):
           get_user_model().objects.create_user('', 'girls754')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
           'olvindiaz@outlook.com',
           'girls754'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)