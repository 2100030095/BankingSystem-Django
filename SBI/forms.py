import datetime

from django import forms
from django.conf import settings

from django import forms
from captcha.fields import CaptchaField
class StudentForm(forms.Form):

    file      = forms.FileField() # for creating file input

class MyForm(forms.Form):
    captcha=CaptchaField()