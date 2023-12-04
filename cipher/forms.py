# forms.py
from django import forms

class MyForm(forms.Form):

    # https://stackoverflow.com/questions/39602903/django-form-how-hide-colon-from-initial-text
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes colon in labels

    # plaintext = forms.CharField(
    # min_length=8,
    # max_length=8,
    # widget=forms.TextInput(attrs={'class': 'cipherInput'}),
    # label="8-Bit plaintext")

    # key = forms.CharField(
    # min_length=10,
    # max_length=10,
    # widget=forms.TextInput(attrs={'class': 'cipherInput'}),
    # label="10-Bit key")
    
class sdesEncryptionForm(forms.Form):
    plaintext = forms.CharField(
    min_length=8,
    max_length=8,
    widget=forms.TextInput(attrs={'class': 'cipherInput encryptInput'}), required=False)

    key = forms.CharField(
    min_length=10,
    max_length=10,
    widget=forms.TextInput(attrs={'class': 'cipherInput encryptInput'}), required=False)

    form_id = forms.CharField(
        widget=forms.HiddenInput(), required=False)
    

class sdesDecryptionForm(forms.Form):
    ciphertext = forms.CharField(
    min_length=8,
    max_length=8,
    widget=forms.TextInput(attrs={'class': 'cipherInput decryptInput'}), required=False)

    # TODO
    # Change all instances of the decryption key to decryptKey to distinguish it from the encryption 'key'
    cipherkey = forms.CharField(
    min_length=10,
    max_length=10,
    widget=forms.TextInput(attrs={'class': 'cipherInput decryptInput'}), required=False)

    form_id = forms.CharField(
        widget=forms.HiddenInput(), required=False)