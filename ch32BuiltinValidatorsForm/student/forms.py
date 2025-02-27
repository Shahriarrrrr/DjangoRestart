from django import forms
from django.core import validators
#Custom Validators
"""For example suppose we want email starting with 's' """

def starts_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Email should start with s')
    




#Builtin Validators
class Registration(forms.Form):
    name  = forms.CharField(validators= [
        validators.MaxLengthValidator(10),
        validators.MinLengthValidator(3)])
    email  = forms.EmailField(validators=[starts_with_s])
    password = forms.CharField(widget= forms.PasswordInput)

