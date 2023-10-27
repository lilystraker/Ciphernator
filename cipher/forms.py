# forms.py
from django import forms

class MyForm(forms.Form):
    plaintext = forms.CharField(
    min_length=8,
    max_length=8,
    widget=forms.TextInput(attrs={'class': 'cipherInput'}),
    label="8-bit plaintext")

    key = forms.CharField(
    min_length=10,
    max_length=10,
    widget=forms.TextInput(attrs={'class': 'cipherInput'}),
    label="10-bit key")
    
