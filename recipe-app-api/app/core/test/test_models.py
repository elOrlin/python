from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        email = 'orlindiaz@outlook.com'
        password = 'girls754'
        user = get_user_model().objects.create_user (
            email=email,
            password=password,
        )

        self.assertEqual(user.email , email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['orlindiaz@outlook.com', 'orlindiaz@outlook.com'],
            ['olvindiaz@outlook.com', 'olvindiaz@outlook.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'olvindiaz123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '123456')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'olvindiaz@outlook.com',
            'olvindiaz123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)