from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from ..models import Category, Product
from django.urls import reverse


User = get_user_model()


class ShopViewTestCase(TestCase):
    def get_user_data(self, num=1):
        return {
            'username': 'username_{}'.format(num),
            'email': 'user{}@example.com'.format(num),
            'password': 'p@ssw0rdUser{}'.format(num),
            'first_name': 'first_name_{}'.format(num),
            'last_name': 'last_name_{}'.format(num),
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
    """
    def login(self, user=None):
        if not user:
            user = self.get_user_data()
        data = {
            'username': user['username'],
            'password': user['password'],
        }
        self.client.login(**data)
    """
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

    def test_product_list(self):
        # self.login()
        cate1 = self.get_category_data()
        prod1 = self.get_product_data()

        path = reverse('shop:product_list')
        resp = self.client.get(path)
        self.assertEqual(resp.status_code, 200)
        path = reverse('shop:product_list_by_category', args=[cate1['slug']])
        resp = self.client.get(path)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, prod1['name'])

    def test_product_detail(self):
        pro1 = self.get_product_data()
        product1 = Product.objects.first()
        self.assertEqual(product1.__str__(), pro1['name'])
        path = reverse('shop:product_detail', args=[product1.id, product1.slug])
        resp = self.client.get(path)
        self.assertEqual(resp.status_code, 200)


