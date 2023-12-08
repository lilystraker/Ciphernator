# Running program
    # Windows
        # myenv\Scripts\activate
        # py manage.py runserver

    # Mac
        # Activate venv environment
        # python3 manage.py runserver

import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader
from .forms import MyForm, sdesEncryptionForm, sdesDecryptionForm, dheForm
from django.shortcuts import render
from itertools import permutations
from .functions.sdesFunctions import generateKey, sdesEncryption, sdesDecipher
<<<<<<< Updated upstream
=======
from .functions.dheFunctions import calculateOutputs, primitive_roots, is_primitive_root
>>>>>>> Stashed changes
import re


def index(request):
    r = requests.get('https://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


# @csrf_exempt
# def encrypt_view(request):
#     k1 = ""
#     k2 = ""
#     ciphertext = ""
#     plaintext = ""
#     key = ""
#     encryption_form = sdesEncryptionForm()
#     if request.method == 'POST':
        
#         print(request.POST)
#         print(encryption_form.errors)
#         if encryption_form.is_valid():

#         # Handle encryption form
#             form = encryption_form
#             key = form.cleaned_data['key']
#             plaintext = form.cleaned_data['plaintext']


#             keys = generateKey(key)
#             k1 = ''.join(keys[0])
#             k2 = ''.join(keys[1])
#             ciphertext = ''.join(sdesEncryption(plaintext, key, keys))
#     else:
#         print("request.method was not POST")

#     print("Plaintext: ", plaintext)
#     print("Key: ", key)
#     print("k1: ", k1)
#     print("k2: ", k2)
#     print("Ciphertext: ", ciphertext)
    
#     return render(request, 'index.html', {
#         'encryption_form': encryption_form,
#         'k1' : k1, 'k2' : k2, 'ciphertext': ciphertext, 'plaintext': plaintext, 'key': key,
#     })


# def decrypt_view(request):
#     k1 = ""
#     k2 = ""
#     ciphertext = ""
#     plaintext = ""
#     key = ""
#     decryption_form = sdesDecryptionForm()
#     if request.method == 'POST' and decryption_form.is_valid():
#         # Handle decryption form
#             form = decryption_form
#             key = form.cleaned_data['key']
#             ciphertext = form.cleaned_data['ciphertext']

#             print(request.POST)
#             print(form.errors)

#             keys = generateKey(key)
#             k1 = ''.join(keys[0])
#             k2 = ''.join(keys[1])
#             plaintext = ''.join(sdesDecipher(ciphertext, key, keys))
#     else:
#         print("request.method was not POST")

#     print("Plaintext: ", plaintext)
#     print("Key: ", key)
#     print("k1: ", k1)
#     print("k2: ", k2)
#     print("Ciphertext: ", ciphertext)
    
#     return render(request, 'index.html', {
#         'decryption_form': decryption_form,
#         'k1' : k1, 'k2' : k2, 'ciphertext': ciphertext, 'plaintext': plaintext, 'key': key,
#     })


def cipher(request):
    k1 = ""
    k2 = ""
    ciphertext = ""
    plaintext = ""
    key = ""
    cipherkey = ""
    form = MyForm()
    form_to_display = request.GET.get('form', 'encryption')  # Default to 'encryption' if no parameter is provided

    # form = sdesEncryptionForm(initial={'form_id': 'encryption'})
    encryption_form = sdesEncryptionForm()
    decryption_form = sdesDecryptionForm()

    if request.method == 'POST':
        encryption_form = sdesEncryptionForm(request.POST)
        decryption_form = sdesDecryptionForm(request.POST)

        if encryption_form.is_valid():
            form_id = encryption_form.cleaned_data['form_id']

            if (form_id == 'encryption'):
                form = encryption_form
                key = form.cleaned_data['key']
                plaintext = form.cleaned_data['plaintext']

                print(request.POST)
                print(form.errors)

                keys = generateKey(key)
                k1 = ''.join(keys[0])
                k2 = ''.join(keys[1])
                ciphertext = ''.join(sdesEncryption(plaintext, key, keys))

        if decryption_form.is_valid():
            form_id = decryption_form.cleaned_data['form_id']

            if (form_id == 'decryption'):
                form = decryption_form
                cipherkey = form.cleaned_data['cipherkey']
                ciphertext = form.cleaned_data['ciphertext']

                print(request.POST)
                print(form.errors)

                keys = generateKey(cipherkey)
                k1 = ''.join(keys[0])
                k2 = ''.join(keys[1])
                plaintext = ''.join(sdesDecipher(ciphertext, cipherkey, keys))
    else:
        print("request.method was not POST")

    print("Plaintext: ", plaintext)
    print("Key: ", key)
    print("Cipherkey: ", cipherkey)
    print("k1: ", k1)
    print("k2: ", k2)
    print("Ciphertext: ", ciphertext)
    
    return render(request, 'index.html', {
        'encryption_form': encryption_form,
        'decryption_form': decryption_form,
        'k1' : k1, 'k2' : k2, 'ciphertext': ciphertext, 'plaintext': plaintext, 'key': key, 'cipherkey': cipherkey,
        'form_to_display': form_to_display,
    })
  
def dhe(request):
    primitive_root = ""
    generator = ""
<<<<<<< Updated upstream
    form = dheForm()
    return render(request, 'dhe.html', {
        'dhe_form': form,
        'primitive_root' : primitive_root, 'generator' : generator,
=======
    xa = ""
    xb = ""
    ya = ""
    yb = ""
    k1 = ""
    k2 = ""
    primitive_roots_list = []
    form = dheForm()

    if request.method == 'POST':
        print("post")
        form = dheForm(request.POST)  # Bind the POST data to the form

        if form.is_valid():
            print("valid")
            prime_modulus = form.cleaned_data['prime_modulus']
            generator = form.cleaned_data['generator']
            xa = form.cleaned_data['xa']
            xb = form.cleaned_data['xb']
            print(request.POST)  # Add this line

            # check whether generator is a primitive root of prime modulus
            if is_primitive_root(int(generator), int(prime_modulus)):
                print("generator valid")

                (ya, yb, k1, k2) = calculateOutputs(int(prime_modulus), int(generator), int(xa), int(xb)) 
            else:
                print("generator INvalid")
                print("generator: ", generator)
                # if not, generate a list of all valid primitive roots
                primitive_roots_list = primitive_roots(int(prime_modulus))
        else:
            print("Form is invalid")
            print(form.errors)
    else:
        print("request.method was not POST")
    return render(request, 'dhe.html', {
        'dhe_form': form,
        'prime_modulus' : prime_modulus, 'generator' : generator, 'xa' : xa, 'xb' : xb, 'ya': ya, 'yb': yb, 'k1': k1, 
        'primitive_roots_list': primitive_roots_list,
>>>>>>> Stashed changes
    })

def contact(request):
    return render(request, 'contact.html')