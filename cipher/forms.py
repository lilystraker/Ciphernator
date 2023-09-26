# forms.py
from django import forms

class MyForm(forms.Form):
    key = forms.CharField(max_length=10)
    plaintext = forms.CharField(max_length=8)