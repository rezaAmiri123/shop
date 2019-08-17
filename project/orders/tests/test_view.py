from django.test import TestCase
from ..models import Order, OrderItem, Coupon
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
User = get_user_model()


class OrderTestCase(TestCase):
    def get_user_data(self, num=1):
        return {
            'username': 'username_{}'.format(num),
            'email': 'user{}@example.com'.format(num),
            'password': 'p@ssw0rdUser{}'.format(num),
            'first_name': 'first_name_{}'.format(num),
            'last_name': 'last_name_{}'.format(num),
            'is_staff': True
        }

    def get_order_data(self, num=1, coupon=None):
        return {
            'first_name': 'first_name_{}'.format(num),
            'last_name': 'last_name_{}'.format(num),
            'email': 'email{}@example.com'.format(num),
            'address': 'address_{}'.format(num),
            'postal_code': '{num}{num}{num}{num}{num}'.format(num=num),
            'city': 'city_{}'.format(num),
            'paid': False,
            'braintree_id': '{num}{num}{num}{num}{num}{num}'.format(num=num),
            'discount': num,
            'coupon': coupon
        }

    def get_coupon_data(self, num=1):
        return {
            'code': 'code_{}'.format(num),
            'valid_from': timezone.now() - timezone.timedelta(num),
            'valid_to': timezone.now() + timezone.timedelta(num),
            'discount': 3 * num,
            'active': True,
        }

    def login(self, user=None):
        if not user:
            user = self.get_user_data()
        data = {
            'username': user['username'],
            'password': user['password'],
        }
        self.client.login(**data)


    def setUp(self):
        user_data = self.get_user_data()
        User.objects.create_user(**user_data)

    def test_order_create(self):
        path = reverse('orders:order_create')
        resp = self.client.get(path)
        self.assertEqual(resp.status_code, 200)

        coup1 = self.get_coupon_data()
        coupon1 = Coupon.objects.create(**coup1)
        ord1 = self.get_order_data(coupon=coupon1)
        resp = self.client.post(path, ord1)
        self.assertEqual(resp.status_code, 302)
        print(resp.status_code)
        print(resp.content)
        # self.assertContains(resp, ord1['email'])




