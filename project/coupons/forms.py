from django import forms
from django.utils.translation import gettext_lazy as _


class CouponApplyForms(forms.Form):
    code = forms.CharField(label=_('Coupon'))
