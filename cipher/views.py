# myenv\Scripts\activate
# py manage.py runserver

from django.http import HttpResponse
from django.template import loader
from .forms import MyForm, sdesEncryptionForm, sdesDecryptionForm
from django.shortcuts import render
from itertools import permutations

def cipher(request):
    k1 = ""
    k2 = ""
    form = MyForm()

    encryption_form = sdesEncryptionForm(request.POST)
    decryption_form = sdesDecryptionForm(request.POST)
    is_encryption_form = False
    is_decryption_form = False
    
    if request.method == 'POST':
        selected_option = request.POST.get('cipherType')

        if selected_option == 'encryption' and encryption_form.is_valid():
            is_encryption_form = True
            key = form.cleaned_data['key']
            plaintext = form.cleaned_data['plaintext']
            k1 = encrypt(key, plaintext)[0]
            k2 = encrypt(key, plaintext)[1]
            # Process the encryption form
        elif selected_option == 'decryption' and decryption_form.is_valid():
            is_edecryption_form = True
            key = form.cleaned_data['key']
            plaintext = form.cleaned_data['plaintext']
            k1 = encrypt(key, plaintext)[0]
            k2 = encrypt(key, plaintext)[1]
            # Process the decryption form

    return render(request, 'index.html', {
        'encryption_form': encryption_form,
        'decryption_form': decryption_form,
    })
  

def p10(key):
    key_list = [num for num in key]

    p10_list = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]

    permutated = []
    column = 0

    for column in range(0, len(p10_list)):
        for num in range(0, len(key_list)):
          if (p10_list[column] == num+1):
              
              permutated.append(key_list[num])
              break
              
    # Result is an array of characters
    return permutated

def p8(key):
    key_list = [num for num in key]

    p8_list = [6, 3, 7, 4, 8, 5, 10, 9]

    permutated = []
    column = 0

    for column in range(0, len(p8_list)):
        for num in range(0, len(key_list)):
          if (p8_list[column] == num+1):
              
              permutated.append(key_list[num])
              break
              
    # Result is an array of characters
    return permutated


def merge(left, right):
    merged_list = []
    for elem in left:
        merged_list.append(elem)
    for elem in right:
        merged_list.append(elem)
    return merged_list

# Assuming input is an array of characters
def ls1(input, shift_amount=1):
    if len(input) <= 1:
        return input  # No change needed for lists with 0 or 1 element

    shift_amount %= len(input)  # Ensure shift_amount is within the range of the list length

    return input[shift_amount:] + input[:shift_amount]



def encrypt(key, plaintext):
    # Perform P10 function
  permutated = p10(key)

  # Split P10 into two 5 bit numbers
  left = permutated[0:5]
  right = permutated[5:10]

  # Left shift both by 1 bit
  left = ls1(left)
  right = ls1(right)

  # Merge them back together 
  merged_list = merge(left, right)

  # Perform P8 function
  # Now we have K1
  k1 = p8(merged_list)

  # Left shift bit twice
  left = ls1(left, 2)
  right = ls1(right, 2)

  merged_list = merge(left, right)

  k2 = p8(merged_list)
  print("k2: ", k2)

  return [k1, k2]
    