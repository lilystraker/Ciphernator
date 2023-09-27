
# Test cases:
#   input: 1011101111
#   output: 1101111110

#   input: 1010101010
#   output: 1101001100

# Input is a 10-bit integer
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

# Perform P10 function
permutated = p10("0010010011")

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
print(k1)

# Left shift bit twice
left = ls1(left, 2)
right = ls1(right, 2)

merged_list = merge(left, right)

k2 = p8(merged_list)
print("k2: ", k2)
