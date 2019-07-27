from django.test import TestCase
from django.urls import reverse
from ..models import Coupon

from .test_models import CouponModelTest


class CouponViewTest(TestCase):
    def setUp(self):
        coupon = CouponModelTest.get_model_data()
        Coupon.objects.create(**coupon)

    def test_post_data(self):
        url = reverse('coupons:apply')
        data = {'code': 'code_1'}

        # send get request
        response = self.client.get(url, data=data)
        # get request not allowed
        self.assertEqual(response.status_code, 405)

        # send post request
        response = self.client.post(url, data=data)
        # response status code must be redirected
        self.assertEqual(response.status_code, 302)
