# Running tests
    # Windows
        # py manage.py test
    # Mac
        # python3 manage.py test

from django.test import TestCase
from cipher.forms import sdesEncryptionForm, sdesDecryptionForm

# Create your tests here.

# Check input labels
class MyTests(TestCase):
    # === SDES === #
    # Test both plaintext and ciphertext inputs for both forms
    def test_plaintext_ciphertext(self):
        test_cases = [
            ('1', False),
            ('00000000', True),
            ('11111111', True),
            ('10', False),
            ('101', False),
            ('1010', False),
            ('10101', False),
            ('101010', False),
            ('1010101', False),
            ('10101010', True),
            ('gggggggg', False),
            ('!@#$%^&*', False),
            ('!', False),
            ('12345678', False),
            ('123', False),
            ('01110101', True),
            ('101010101', False),
            ('1010101010', False),
            ('0000000', False),  # Only 7 digits
            ('000000000', False),  # 9 digits
            ('abcdefgh', False),  # Not a binary number
        ]

        for ciphertext, expected_validity in test_cases:
            with self.subTest(ciphertext=ciphertext):
                form_data = {'ciphertext': ciphertext}
                form = sdesDecryptionForm(data=form_data)
                self.assertEqual(form.is_valid(), expected_validity)

        for plaintext, expected_validity in test_cases:
            with self.subTest(plaintext=plaintext):
                form_data = {'plaintext': plaintext}
                form = sdesEncryptionForm(data=form_data)
                self.assertEqual(form.is_valid(), expected_validity)


    # Test key input for both forms
    def test_keys(self):
        test_cases = [
            ('1', False),
            ('0000000000', True),
            ('1111111111', True),
            ('10', False),
            ('101', False),
            ('1010', False),
            ('10101', False),
            ('101010', False),
            ('1010101', False),
            ('10101010', False),
            ('101010101', False),
            ('1010101010', True),
            ('gggggggggg', False),
            ('!@#$%^&***', False),
            ('!', False),
            ('1234567890', False),
            ('123', False),
            ('0111010111', True),
            ('10101010110', False),
            ('101010101001', False),
            ('0000000', False),  # Only 7 digits
            ('00000000000', False),  # 11 digits
            ('abcdefgh', False),  # Not a binary number
        ]

        for key, expected_validity in test_cases:
            with self.subTest(key=key):
                form_data = {'key': key}
                form = sdesEncryptionForm(data=form_data)
                self.assertEqual(form.is_valid(), expected_validity)

        for cipherkey, expected_validity in test_cases:
            with self.subTest(cipherkey=cipherkey):
                form_data = {'cipherkey': cipherkey}
                form = sdesDecryptionForm(data=form_data)
                self.assertEqual(form.is_valid(), expected_validity)


 






    

