# forms.py
from django import forms

class MyForm(forms.Form):
    key = forms.CharField(min_length=10, max_length=10)
    plaintext = forms.CharField(min_length=8,max_length=8)