# forms.py
from django import forms
from django.core.validators import RegexValidator


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
        validators=[
            RegexValidator(
                regex='^[01]{8}$'  # 8 digit binary number
            )
        ],
        min_length=8,
        max_length=8,
        widget=forms.TextInput(attrs={'class': 'cipherInput encryptInput'}), required=False)

    key = forms.CharField(
        validators=[
            RegexValidator(
                regex='^[01]{10}$'  # 8 digit binary number
            )
        ],
    min_length=10,
    max_length=10,
    widget=forms.TextInput(attrs={'class': 'cipherInput encryptInput'}), required=False)

    form_id = forms.CharField(
        widget=forms.HiddenInput(), required=False)
    

class sdesDecryptionForm(forms.Form):
    ciphertext = forms.CharField(
        validators=[
            RegexValidator(
                regex='^[01]{8}$'  # 8 digit binary number
            )
        ],
    min_length=8,
    max_length=8,
    widget=forms.TextInput(attrs={'class': 'cipherInput decryptInput'}), required=False)

    cipherkey = forms.CharField(
        validators=[
            RegexValidator(
                regex='^[01]{10}$'  # 8 digit binary number
            )
        ],
    min_length=10,
    max_length=10,
    widget=forms.TextInput(attrs={'class': 'cipherInput decryptInput'}), required=False)

    form_id = forms.CharField(
        widget=forms.HiddenInput(), required=False)
    

    
class dheForm(forms.Form):
    primitive_root = forms.CharField(
        # validators=[
        #     RegexValidator(
        #         regex='^[01]{8}$'  # 8 digit binary number
        #     )
        # ],
        min_length=5,
        max_length=5,
        widget=forms.TextInput(attrs={'class': 'cipherInput encryptInput'}), required=False)

    generator = forms.CharField(
        # validators=[
        #     RegexValidator(
        #         regex='^[01]{10}$'  # 8 digit binary number
        #     )
        # ],
    min_length=3,
    max_length=3,
    widget=forms.TextInput(attrs={'class': 'cipherInput encryptInput'}), required=False)

    form_id = forms.CharField(
        widget=forms.HiddenInput(), required=False)
    
