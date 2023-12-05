# Running tests
    # Windows
        # py manage.py test
    # Mac
        # python3 manage.py test

from django.test import TestCase
from cipher.forms import sdesEncryptionForm, sdesDecryptionForm
from cipher.views import generateKey, sdesEncryption, sdesDecipher  # Import your encryption function

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

    # check that the encryption and decryption functions produce the correct outputs
    def test_encryption(self):
        # (plaintext, key, k1, k2, ciphertext)
        test_cases = [
            ('11110110', '1101000100',  '10011000', '10000101', '00001010'),
            ('01111111', '0010100100', '00001100', '11010000', '11011011'),
            ('10000111', '0111010101', '00011111', '11101100', '10110010'),
            ('10111101', '0110011010', '01100101', '01100110', '01010000'),
            ('00001010', '0010100000', '00000100', '01010000', '11110111'),
            ('01110001', '1111010111', '10111111', '11101111', '10000011'),
            ('11000110', '1101001011', '11110010', '00001111', '01110011'),
            ('10100000', '0111000000', '00010100', '01000100', '01010100')
        ]

        for plaintext, key, k1, k2, ciphertext in test_cases:
            # test encryption
            with self.subTest(plaintext=plaintext, key=key):
                keys = generateKey(key)
                k1 = ''.join(keys[0])
                k2 = ''.join(keys[1])
                result = ''.join(sdesEncryption(plaintext, key, keys))
                self.assertEqual(result, ciphertext)
            # test decryption
            with self.subTest(ciphertext=ciphertext, key=key):
                keys = generateKey(key)
                k1 = ''.join(keys[0])
                k2 = ''.join(keys[1])
                result = ''.join(sdesDecipher(ciphertext, key, keys))
                self.assertEqual(result, plaintext)



 






    

