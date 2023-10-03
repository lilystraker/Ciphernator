
import re
# 
p10_list = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
ip_list = [2, 6, 3, 1, 4, 8, 5, 7]
inverse_ip_list = [4, 1, 3, 5, 7, 2, 8, 6]
p8_list = [6, 3, 7, 4, 8, 5, 10, 9]
ep_list = [4, 1, 2, 3, 2, 3, 4, 1]
p4_list = [2, 4, 3, 1]
s0_list = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
s1_list = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]


def permutate(input, list):
    key_list = [num for num in input]

    permutated = []
    column = 0

    for column in range(0, len(list)):
        for num in range(0, len(key_list)):
          if (list[column] == num+1):
              
              permutated.append(key_list[num])
              break
              
    # Result is an array of characters
    return permutated

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


def generateKey(key):
    # print input key
    # print("10-bit Key: ", key)
    # Perform P10 function
    permutated = permutate(key, p10_list)

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
    k1 = permutate(merged_list, p8_list)
  

    # Left shift bit twice
    left = ls1(left, 2)
    right = ls1(right, 2)

    merged_list = merge(left, right)

    k2 = permutate(merged_list, p8_list)


    return [k1, k2]


def exclusiveOr(binary1, binary2):
    # binary1str = ''.join(binary1)
    # binary2str = ''.join(binary2)

    XOR_result = []
    for num in range(len(binary1)):
        if (binary1[num] == binary2[num]):
            XOR_result.append("0")
        else:
            XOR_result.append("1")

    return XOR_result

def s_matrix(input, matrix):
    # input = 0111

    # row = b1b4
    row = input[0]
    row += input[3]
    row = int(row, 2)
    # col = b2b3
    col = input[1]
    col += input[2]
    col = int(col, 2)
    # find 1st row, 3rd col of s0 = 0
    s0_result = matrix[row][col]
    
    binary_result = bin(s0_result)[2:]

    # add leading 0 if lost
    if (len(binary_result) == 1):
        binary_result = format(s0_result, '02b')
    # convert to binary
    return binary_result

def sdesEncryption(plaintext, key, keys):
    k1 = keys[0]
    k2 = keys[1]

    ip = permutate(plaintext, ip_list)
    fk = ip[0:4]
    rightIP = ip[4:8]
    
    ep = permutate(rightIP, ep_list)
    XOR = exclusiveOr(ep, k1)

    s0_result = s_matrix(XOR[0:4], s0_list)

    s1_result = s_matrix(XOR[4:8], s1_list)
    s_result = []
    s_result = s0_result + s1_result
    p4 = permutate(s_result, p4_list)
    XOR = exclusiveOr(fk, p4)

    sw = rightIP + XOR[0:4]
    fk = sw[0:4]
    rightsw = sw[4:8]
    ep = permutate(rightsw, ep_list)
    xor = exclusiveOr(ep, k2)
    s0_result = s_matrix(xor[0:4], s0_list)
    s1_result = s_matrix(xor[4:8], s1_list)
    s_result = []
    s_result = s0_result + s1_result
    p4 = permutate(s_result, p4_list)
    xor = exclusiveOr(fk, p4)
    result = xor + rightsw
    inverse_ip = permutate(result, inverse_ip_list)
    # Print all inputs and outputs
    printOutput(plaintext, inverse_ip, key, keys)


def sdesDecipher(ciphertext, key, keys):
    k1 = keys[0]
    k2 = keys[1]
    # perform IP
    ip = permutate(ciphertext, ip_list)
    # Apply E/P on right bits
    ep = permutate(ip[4:8], ep_list)
    
    # perform XOR on ep and k2
    xor = exclusiveOr(k2, ep)

    s0_result = s_matrix(xor[0:4], s0_list)
    s1_result = s_matrix(xor[4:8], s1_list)

    s_result = s0_result + s1_result
    p4 = permutate(s_result, p4_list)
    xor = exclusiveOr(p4, ip[0:4])
    ip[0:4] = xor
    # SWAP
    new_ip = ip[4:8] + ip[0:4]
    # ep to right 4 bits
    ep = permutate(new_ip[4:8], ep_list)
    xor1 = exclusiveOr(ep, k1)

    s0_result = s_matrix(xor1[0:4], s0_list)
    s1_result = s_matrix(xor1[4:8], s1_list)

    s_result = s0_result + s1_result
    p4 = permutate(s_result, p4_list)
    xor = exclusiveOr(p4, ip[4:8])
    new_result = xor + ip[0:4]


    IP = permutate(new_result, inverse_ip_list)
    printOutput(''.join(IP), ciphertext, key, keys)

def checkKey(key):
    keyRegex = "^[0-1]{10}$"
    if (re.match(keyRegex, key)):
        keyValid = True
    else:
        keyValid = False
    return keyValid

def checkInput(input):
    inputRegex = "^[0-1]{8}$"
    if (re.match(inputRegex, input)):
        inputValid = True
    else:
        inputValid = False
    return inputValid

def printOutput(plaintext, ciphertext, key, keys):
    print("\nOutputs:")
    print("\tKey:\n\t\t", key)
    print("\tPlaintext:\n\t\t", plaintext)
    print("\tK1:\n\t\t", ''.join(keys[0]))
    print("\tK2:\n\t\t", ''.join(keys[1]))
    print("\tCiphertext:\n\t\t", ''.join(ciphertext))

def main():
    print("S-DES Cipher Encryption and Decryption\n")
    cipherChosen = False
    while (cipherChosen == False):
        print("Input 'x' to exit\n")
        cipher = input("Encrypt (e) or Decrypt (d)?\n")
        keyValid = False
        plaintextValid = False
        
        if (cipher.lower() == 'e'):
            while (keyValid == False):
                key = input("Enter a 10-bit key\n")
                
                keyValid = checkKey(key)

                if (keyValid):
                    keys = generateKey("0010010011")
                    cipherChosen = True
                elif (key == 'x'):
                    print("Quitting program.")
                    cipherChosen = True
                    plaintextValid = True
                    break
                else:
                    print("Please enter a valid 10-bit key in binary")

            while (plaintextValid == False):
                plaintext = input("Enter an 8-bit plaintext\n")

                plaintextValid = checkInput(plaintext)

                if (plaintextValid):
                    cipherChosen = True
                    # 8-bit plaintext
                    sdesEncryption(plaintext, key, keys)
                elif (plaintext == 'x'):
                    print("Quitting program.")
                    cipherChosen = True
                    plaintextValid = True
                    break
                else:
                    print("Please enter a valid 8-bit plaintext in binary")

        elif (cipher.lower() == 'd'):
            keyValid = False
            ciphertextValid = False
        
            while (keyValid == False):
                key = input("Enter a 10-bit key\n")
                
                keyValid = checkKey(key)

                if (keyValid):
                    keys = generateKey("0010010011")
                    cipherChosen = True
                elif (key == 'x'):
                    print("Quitting program.")
                    cipherChosen = True
                    ciphertextValid = True
                    break
                else:
                    print("Please enter a valid 10-bit key in binary")

            while (ciphertextValid == False):
                ciphertext = input("Enter an 8-bit ciphertext\n")

                ciphertextValid = checkInput(ciphertext)

                if (ciphertextValid):
                    cipherChosen = True
                    # 8-bit plaintext
                    sdesDecipher(ciphertext, key, keys)
                elif (ciphertext == 'x'):
                    print("Quitting program.")
                    cipherChosen = True
                    ciphertextValid = True
                    break
                else:
                    print("Please enter a valid 8-bit ciphertext in binary")
        elif (cipher.lower() == 'x'):
            print("Quitting program.")
            cipherChosen = True
        else:
            print("Please enter 'e' or 'd'")


main()



