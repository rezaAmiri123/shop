from django.test import TestCase
from ..forms import CouponApplyForms


class CouponFormTest(TestCase):

    def test_form(self):
        data = {'code': 'coupon1'}
        form = CouponApplyForms(data=data)
        self.assertTrue(form.is_valid())
        cd = {}
        if form.is_valid():
            cd = form.cleaned_data
        self.assertEqual(cd['code'], data['code'])
        self.assertNotEqual(cd['code'], data['code'] + '1')
