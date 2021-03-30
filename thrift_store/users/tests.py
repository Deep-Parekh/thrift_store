from django.test import TestCase
from django.contrib.auth import get_user_model

'''
class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='foo', password='bar')
        self.assertEqual(user.username, 'foo')
        # self.assertTrue(user.is_active)
        # self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            # self.assertIsNone(user.username)
            pass
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('super_foo', 'bar')
        self.assertEqual(admin_user.email, 'super_foo')
        # self.assertTrue(admin_user.is_active)
        # self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            # self.assertIsNone(admin_user.username)
            pass
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='supe_foo', password='bar', is_superuser=False
            )
'''
