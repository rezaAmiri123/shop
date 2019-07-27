from django.test import TestCase

# Create your tests here.
from ..models import Coupon
from django.utils import timezone


class CouponModelTest(TestCase):

    @staticmethod
    def get_model_data(num=1, discount=33, valid_from=0, valid_to=100, active=True):
        valid_from = timezone.now() + timezone.timedelta(minutes=valid_from)
        valid_to = timezone.now() + timezone.timedelta(minutes=valid_to)

        return {
            'code': 'code_{}'.format(num),
            'valid_from': valid_from,
            'valid_to': valid_to,
            'discount': discount,
            'active': active,
        }

    def test_str(self):
        coupon1 = self.get_model_data()
        Coupon.objects.create(**coupon1)
        coupon = Coupon.objects.get(id=1)
        self.assertEqual(coupon.__str__(), coupon1['code'])

    def test_discount(self):
        coupon1 = self.get_model_data(discount=101)
        Coupon.objects.create(**coupon1)
        coupon = Coupon.objects.get(id=1)

        

