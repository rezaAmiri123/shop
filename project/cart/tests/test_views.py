from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from coupons.models import Coupon
from orders.models import Order
from shop.models import Product, Category
from django.urls import reverse

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


    def get_category_data(self, num=1):
        return {
            'name': 'category_{}'.format(num),
            'slug': 'category_{}'.format(num),
        }

    def get_product_data(self, num=1, category=None):
        return {
            'name': 'product_{}'.format(num),
            'slug': 'product_{}'.format(num),
            'category': category,
            'price': num * 24 + 100,
            'available': True
        }


    def setUp(self):
        user_data = self.get_user_data()
        User.objects.create_user(**user_data)

        cate1 = self.get_category_data()
        Category.objects.create(**cate1)
        language = settings.LANGUAGE_CODE
        category1 = Category.objects.get(translations__language_code=language,
                                         translations__name=cate1['name'])
        prod1 = self.get_product_data(category=category1)
        Product.objects.create(**prod1)

    def cart_add(self):
        # self.login()

        car1 = self.get_cart_data()
        product1 = Product.objects.first()
        path = reverse('cart:cart_add', args=[product1.id])
        self.client.post(path, car1)
        # self.assertEqual(resp.status_code, 302)

    def test_remove_cart(self):
        self.login()
        self.cart_add()
        product1 = Product.objects.first()
        path = reverse('cart:cart_remove', args=[product1.id])
        resp = self.client.get(path)
        self.assertEqual(resp.status_code, 302)

    def test_cart_detail(self):
        self.login()
        self.cart_add()
        path = reverse('cart:cart_detail')
        resp = self.client.get(path)
        self.assertEqual(resp.status_code, 200)


