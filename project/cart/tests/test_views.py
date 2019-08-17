from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model


User = get_user_model()


class ViewTestCase(TestCase):
    def get_user_data(self, num=1):
        return {
            'username': 'username_{}'.format(num),
            'email': 'user{}@example.com'.format(num),
            'password': 'p@ssw0rdUser{}'.format(num),
            'first_name': 'first_name_{}'.format(num),
            'last_name': 'last_name_{}'.format(num),
        }

    def login(self, user=None):
        if not user:
            user = self.get_user_data()
        data = {
            'username': user['username'],
            'password': user['password'],
        }
        self.client.login(**data)

    def get_cart_data(self, num=1):
        return {
            'quantity': num,
            'update': False
        }

    def setUp(self):
        user_data = self.get_user_data()
        User.objects.create_user(**user_data)

    def test_cart_add(self):
        self.login()


