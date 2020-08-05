from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTestCase(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test creating a new user with an email is successfull"""
        email = 'test@reciope.com'
        password = 'fghdjdkri'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@NXKSJDK>COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='zbmznzss'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@reciopcce.com',
            'fghdjdkricc'
        )
        self.assertTrue(user.is_superuser, True)
        self.assertTrue(user.is_staff, True)
