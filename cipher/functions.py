

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
    print("k1: ", k1)

    # Left shift bit twice
    left = ls1(left, 2)
    right = ls1(right, 2)

    merged_list = merge(left, right)

    k2 = permutate(merged_list, p8_list)
    print("k2: ", k2)

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
    print(row, col)
    # find 1st row, 3rd col of s0 = 0
    s0_result = matrix[row][col]
    
    binary_result = bin(s0_result)[2:]

    # add leading 0 if lost
    if (len(binary_result) == 1):
        binary_result = format(s0_result, '02b')
    # convert to binary
    return binary_result

def sdesEncryption(plaintext, keys):
    k1 = keys[0]
    k2 = keys[1]

    ip = permutate(plaintext, ip_list)
    print("ip: ", ip)
    fk = ip[0:4]
    rightIP = ip[4:8]
    print("right IP: ", rightIP)
    
    ep = permutate(rightIP, ep_list)
    print("E/P: ", ep)
    XOR = exclusiveOr(ep, k1)
    print("XOR: ", XOR)

    s0_result = s_matrix(XOR[0:4], s0_list)
    print("S0 result: ", s0_result)

    s1_result = s_matrix(XOR[4:8], s1_list)
    print("S1 result: ", s1_result)
    s_result = []
    s_result = s0_result + s1_result
    print(s_result)
    p4 = permutate(s_result, p4_list)
    print("P4: ", p4)
    XOR = exclusiveOr(fk, p4)
    print(XOR)

    sw = rightIP + XOR[0:4]
    print("SW: ", sw)
    fk = sw[0:4]
    rightsw = sw[4:8]
    ep = permutate(rightsw, ep_list)
    print("EP: ", ep)
    xor = exclusiveOr(ep, k2)
    s0_result = s_matrix(xor[0:4], s0_list)
    s1_result = s_matrix(xor[4:8], s1_list)
    s_result = []
    s_result = s0_result + s1_result
    p4 = permutate(s_result, p4_list)
    xor = exclusiveOr(fk, p4)
    result = xor + rightsw
    print(result)
    inverse_ip = permutate(result, inverse_ip_list)
    print("Ciphertext: ", inverse_ip)

def sdesDecipher(ciphertext, keys):
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
    print("XOR1: ", xor1)

    s0_result = s_matrix(xor1[0:4], s0_list)
    s1_result = s_matrix(xor1[4:8], s1_list)

    s_result = s0_result + s1_result
    p4 = permutate(s_result, p4_list)
    xor = exclusiveOr(p4, ip[4:8])
    print(xor)
    new_result = xor + ip[0:4]
    print(new_result)

    IP = permutate(new_result, inverse_ip_list)
    print(IP)

keys = generateKey("1010000010")
sdesEncryption("10010111", keys)
# correct !!!
sdesDecipher("00111000", keys)

