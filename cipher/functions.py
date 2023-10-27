# Lily Straker
# 22052506
# INFO3006 - Information Security
# Practical Assignment - Task One - S-DES Encryption and Decryption

import re
# All permutation and s matrixes defined

p10_list = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
ip_list = [2, 6, 3, 1, 4, 8, 5, 7]
inverse_ip_list = [4, 1, 3, 5, 7, 2, 8, 6]
p8_list = [6, 3, 7, 4, 8, 5, 10, 9]
ep_list = [4, 1, 2, 3, 2, 3, 4, 1]
p4_list = [2, 4, 3, 1]
s0_list = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
s1_list = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

def permutate(input, list):
    """ Produces a permutated array 
    (used for P10, P8, IP, IP-1, EP, and P4 functions)"""

    # Turn the binary input into an array of bits
    key_list = [num for num in input]

    # Initialise variables 
    permutated = []
    column = 0

    # Go through each number in the permutation list
    # If the number matches the current column index
    # of the input array, add the corresponding value 
    # to the resulting permutation array
    for column in range(0, len(list)):
        for num in range(0, len(key_list)):
          if (list[column] == num+1):
              permutated.append(key_list[num])
              break
              
    # Result is an array of characters (bits)
    return permutated

def ls(input, shift_amount=1):
    """ Left Shift function 
    Move all bits in the input to the left """
    # Leave 1 bit numbers unaltered
    if len(input) <= 1:
        return input

    # Move the first part of the list to the end of the list (depending on the shift amount)
    return input[shift_amount:] + input[:shift_amount]


def generateKey(key):
    """ Generate K1 and K2 keys """
    # Perform P10 function on input key
    permutated = permutate(key, p10_list)
    # Split P10 into two 5 bit numbers
    left = permutated[0:5]
    right = permutated[5:10]
    # Left shift both by 1 bit
    left = ls(left)
    right = ls(right)

    # Perform P8 function to get K1
    k1 = permutate(left + right, p8_list)

    # Left shift bit twice
    left = ls(left, 2)
    right = ls(right, 2)

    # Perform P8 function to get K2
    k2 = permutate(left + right, p8_list)

    # Return list containing strings K1 and K2
    return [k1, k2]


def exclusiveOr(binary1, binary2):
    """ Perform an XOR operation on two binary numbers """

    XOR_result = []
    # Go through each number in both binary numbers
    # If the numbers match, add a 0 to the resulting array
    # If they do not match, add a 1 to the resulting array
    for num in range(len(binary1)):
        if (binary1[num] == binary2[num]):
            XOR_result.append("0")
        else:
            XOR_result.append("1")

    # Array of strings to make up a binary number
    return XOR_result

def s_matrix(input, matrix):
    """ Find the corresponding coordinate 
    of the s-matrix - Used for S0 and S1 matrices"""

    # Row = b1b4
    row = input[0]
    row += input[3]
    # Convert from binary to integer
    row = int(row, 2)
    # Col = b2b3
    col = input[1]
    col += input[2]
    # Convert from binary to integer
    col = int(col, 2)
    # Find the coordinate from the defined s-matrix
    s0_result = matrix[row][col]
    
    # Convert result back to binary (remove 0b from binary number)
    binary_result = bin(s0_result)[2:]

    # Add back leading 0 if lost
    if (len(binary_result) == 1):
        binary_result = format(s0_result, '02b')

    # Return binary number
    return binary_result

def sdesEncryption(plaintext, key, keys):
    """ S-DES Encryption function using input plaintext and input key """
    # Get K1 and K2
    k1 = keys[0]
    k2 = keys[1]

    # Find IP    
    ip = permutate(plaintext, ip_list)

    # fk is left 4 bits of IP
    fk = ip[0:4]
    rightIP = ip[4:8]
    
    # Calculate EP on right 4 bits
    ep = permutate(rightIP, ep_list)

    # Perform XOR operation on EP and K1
    XOR = exclusiveOr(ep, k1)

    # Use S0 matrix on left 4 bits
    s0_result = s_matrix(XOR[0:4], s0_list)

    # Use S1 matrix on right 4 bits
    s1_result = s_matrix(XOR[4:8], s1_list)

    s_result = []
    # Put results from S0 and S1 together
    s_result = s0_result + s1_result

    # Use P4  
    p4 = permutate(s_result, p4_list)
    # Perform XOR operation on fk and P4
    XOR = exclusiveOr(fk, p4)

    # SW combines right 4 bits of IP and left 4 bits of XOR operation
    # It swaps their positioning 
    # Process repeats for K2
    sw = rightIP + XOR[0:4]
    # redefine fk as left 4 bits of SW
    fk = sw[0:4]
    rightsw = sw[4:8]
    # Find E/P of right 4 bits of SW
    ep = permutate(rightsw, ep_list)
    # Perform XOR operation on EP and K2
    xor = exclusiveOr(ep, k2)
    # Find S0 and S1 matrix coordinates
    s0_result = s_matrix(xor[0:4], s0_list)
    s1_result = s_matrix(xor[4:8], s1_list)
    s_result = []
    s_result = s0_result + s1_result
    # Find P4 of S matrices results
    p4 = permutate(s_result, p4_list)
    # Perform XOR operation on fk and P4
    xor = exclusiveOr(fk, p4)
    result = xor + rightsw
    # Find IP-1
    inverse_ip = permutate(result, inverse_ip_list)

    # Print all inputs and outputs
    printOutput(plaintext, inverse_ip, key, keys)


def sdesDecipher(ciphertext, key, keys):
    """S-DES Decryption function using input ciphertext and input key"""
    # Following this process: http://www.facweb.iitkgp.ac.in/~shamik/spring2007/i&ss/papers/S-DES%20Decryption%20template.htm
    # Unwrap keys from list
    k1 = keys[0]
    k2 = keys[1]
    # Perform IP
    ip = permutate(ciphertext, ip_list)
    # Apply E/P on right bits
    ep = permutate(ip[4:8], ep_list)
    
    # Perform XOR on E/P and K2
    xor = exclusiveOr(k2, ep)

    # Find S-matrix coordinate values
    s0_result = s_matrix(xor[0:4], s0_list)
    s1_result = s_matrix(xor[4:8], s1_list)

    s_result = s0_result + s1_result

    # Find P4 on S-matrix results 
    p4 = permutate(s_result, p4_list)
    # XOR operation on P4 and left 4 bits of IP result
    xor = exclusiveOr(p4, ip[0:4])
    ip[0:4] = xor
    # Swap left and right side 
    new_ip = ip[4:8] + ip[0:4]
    # E/P on right 4 bits of swapped value
    ep = permutate(new_ip[4:8], ep_list)

    # Repeat process for K1
    # Perform XOR on E/P and K1
    xor1 = exclusiveOr(ep, k1)
    # Find S-matrix coordinate values
    s0_result = s_matrix(xor1[0:4], s0_list)
    s1_result = s_matrix(xor1[4:8], s1_list)
    s_result = s0_result + s1_result
    # Use P4 on S-matrix result
    p4 = permutate(s_result, p4_list)
    # Perform XOR on P4 and right 4 bits of old IP result
    xor = exclusiveOr(p4, ip[4:8])
    # Put XOR result and left 4 bits of IP result together
    new_result = xor + ip[0:4]

    # Use inverse IP permutation on this result 
    IP = permutate(new_result, inverse_ip_list)

    # Print results
    printOutput(''.join(IP), ciphertext, key, keys)

def checkInput(input, regex):
    """ Check the validity of input values using regex """
    return bool(re.match(regex, input))

def printOutput(plaintext, ciphertext, key, keys):
    """ Print all inputs and outputs to console """
    print("\nOutputs:")
    print("\tKey:\n\t\t", key)
    print("\tPlaintext:\n\t\t", plaintext)
    # Convert K1, K2, and ciphertext from list to string
    print("\tK1:\n\t\t", ''.join(keys[0]))
    print("\tK2:\n\t\t", ''.join(keys[1]))
    print("\tCiphertext:\n\t\t", ''.join(ciphertext))

    # Condensed printing output used for testing  
    # print("Key:", key, "Plaintext:", plaintext, "K1:", ''.join(keys[0]), "K2:", ''.join(keys[1]), "Ciphertext:", ''.join(ciphertext))


def main():
    """ Show menu when program begins """

    print("S-DES Cipher Encryption and Decryption\n")
    cipherChosen = False
    # Wait for user to select encryption or decryption option
    while (cipherChosen == False):
        print("Input 'x' to exit\n")
        cipher = input("Encrypt (e) or Decrypt (d)?\n")
        keyValid = False
        plaintextValid = False
        
        # Encrpytion selected
        if (cipher.lower() == 'e'):
            # Check the user has inputted a valid 10-bit binary value
            while (keyValid == False):
                key = input("Enter a 10-bit key\n")
                # Define regex for 10-bit binary number
                keyValid = checkInput(key, "^[0-1]{10}$")
                # If input is valid, generate the keys 
                if (keyValid):
                    keys = generateKey(key)
                    cipherChosen = True
                # If user wants to exit program, then quit 
                elif (key == 'x'):
                    print("Quitting program.")
                    cipherChosen = True
                    plaintextValid = True
                    break
                # If user enters an invalid input
                else:
                    print("Please enter a valid 10-bit key in binary")
            
            # Prompt user for input plaintext
            while (plaintextValid == False):
                plaintext = input("Enter an 8-bit plaintext\n")
                # Check user has inputted a valid 8-bit binary number
                plaintextValid = checkInput(plaintext, "^[0-1]{8}$")
                # If input is valid, perform encryption 
                if (plaintextValid):
                    cipherChosen = True
                    sdesEncryption(plaintext, key, keys)
                # Quit program
                elif (plaintext == 'x'):
                    print("Quitting program.")
                    cipherChosen = True
                    plaintextValid = True
                    break
                # If input is invalid, prompt user again
                else:
                    print("Please enter a valid 8-bit plaintext in binary")
        # Decryption selected
        elif (cipher.lower() == 'd'):
            keyValid = False
            ciphertextValid = False
            # Prompt user for key
            while (keyValid == False):
                key = input("Enter a 10-bit key\n")
                # Check input is valid
                keyValid = checkInput(key, "^[0-1]{10}$")
                # If it is valid, generate keys
                if (keyValid):
                    keys = generateKey(key)
                    cipherChosen = True
                # Quit program 
                elif (key == 'x'):
                    print("Quitting program.")
                    cipherChosen = True
                    ciphertextValid = True
                    break
                # If input is invalid, prompt user for another key
                else:
                    print("Please enter a valid 10-bit key in binary")
            # Prompt user for ciphertext
            while (ciphertextValid == False):
                ciphertext = input("Enter an 8-bit ciphertext\n")
                # Check ciphertext is valid 8-bit binary value
                ciphertextValid = checkInput(ciphertext, "^[0-1]{8}$")
                # If input is valid, decrypt the ciphertext
                if (ciphertextValid):
                    cipherChosen = True
                    sdesDecipher(ciphertext, key, keys)
                # Quit program
                elif (ciphertext == 'x'):
                    print("Quitting program.")
                    cipherChosen = True
                    ciphertextValid = True
                    break
                # Prompt user for another ciphertext if invalid
                else:
                    print("Please enter a valid 8-bit ciphertext in binary")
        # Quit program
        elif (cipher.lower() == 'x'):
            print("Quitting program.")
            cipherChosen = True
        # If user enters any other character, prompt them to select the cipher again
        else:
            print("Please enter 'e' or 'd'")

# Run the program
main()



