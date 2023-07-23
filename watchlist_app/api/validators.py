from django.db import models
from django import forms


def preventDecimalNumber(val):
    if val%1!=0 :
        raise forms.ValidationError('The value must be integer.', code=400)

    return val
