#  Diffie-Helman Exchange Key Algorithm

# QUESTIONS

# - We don't have to implement decryption right?
# - Documentation: is my test plan and test documentation okay?
# - Decimal form?

import random
from math import gcd
import math

def is_primitive_root(g, n):
    if gcd(g, n) != 1:
        return False

    totient = n - 1  # Euler's totient function for prime n
    prime_factors = set()

    # Find the prime factors of totient
    for i in range(2, int(totient**0.5) + 1):
        while totient % i == 0:
            prime_factors.add(i)
            totient //= i
        if totient == 1:
            break
    if totient > 1:
        prime_factors.add(totient)

    # Check if g is a primitive root
    for p in prime_factors:
        # if pow(g, (n - 1) // p, n) == 1:
        if (squareAndMultiply(g, (n - 1) // p, n)) == 1:
            return False

    return True

def primitive_roots(n):
    primitive_roots_list = []
    if n == 2:
        return primitive_roots_list
    primitive_roots_list = [g for g in range(1, n) if is_primitive_root(g, n)]
    return primitive_roots_list

# def square_and_multiply(base, exponent, modulus=None):
#     result = 1
    
#     if modulus is not None:
#         base = base % modulus  # Reduce the base if a modulus is provided
#     print(exponent)
#     while exponent > 0:
#         # If the current exponent bit is 1, multiply the result by the base
#         if exponent % 2 == 1:
#             result = (result * base) % modulus if modulus is not None else result * base
        
#         # Square the base and halve the exponent
#         base = (base * base) % modulus if modulus is not None else base * base
#         exponent //= 2
    
#     return result

# def squareAndMultiply(base, exponent, modulus=None):
#     result = 1
#     isFirstOne = False
#         # decimal -> binary (0bxxxx) -> xxxx
#     binary_exponent = bin(exponent)[2:]

#     for bit in binary_exponent:
#         if not(isFirstOne) and bit == "1":
#             isFirstOne = True
#             result = base
#         elif isFirstOne and bit == "1":
#             result = (result * result * base) % modulus if modulus is not None else result * result * base
#         # 0 bit
#         else:
#             # square
#             result = (result * result) % modulus if modulus is not None else result * base
#     return result
        

def squareAndMultiply(base, exponent, modulus=None):
    result = base

        # decimal -> binary (0bxxxx) -> xxxx
    binary_exponent = bin(exponent)[2:]

    for index in range(1, len(binary_exponent)):
        if binary_exponent[index] == "1":
            result = (result * result * base) % modulus if modulus is not None else result * result * base
        # 0 bit
        else:
            # square
            result = (result * result) % modulus if modulus is not None else result * base
    return result



def isPrime(p):
    """ Check whether the prime modulus is prime """
    if p <= 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False

    # floor of the square root of p
    max_divisor = math.isqrt(p)
    for i in range(3, max_divisor + 1, 2):
        if p % i == 0:
            return False

    return True


def isInt(input):
    try:
        int(input)
        return True
    except ValueError:
        print("That is not a valid integer")
        return False

def randomGeneration(min=1, max=99):
    # min <= random_int <= max
    random_int = random.randint(min, max)
    return random_int

def calculateOutputs(p, g, xa, xb):
    ya = squareAndMultiply(g, xa, p)
    yb = squareAndMultiply(g, xb, p)
    k1 = squareAndMultiply(yb, xa, p)
    k2 = squareAndMultiply(ya, xb, p)

    print("k1:", k1)
    print("k2:", k2)

def main():
    print("Diffie-Helman Exchange Key Algorithm")
    print("Press 'x' to exit program")

    canProgramExit = False

    while (not(canProgramExit)):
        # get p value
        pIsValid = False
        gIsValid = False
        xaIsValid = False
        xbIsValid = False

        isAuto = False
        isManual = False
        isSelectionChosen = False
        while (not(isSelectionChosen)):
            s = input("Do you want to automatically generate inputs (y/n)? ")
            if (s.lower() == 'y'):
                isAuto = True
                isSelectionChosen = True
            elif(s.lower() == 'n'):
                isManual = True
                isSelectionChosen = True
            elif(s.lower() == 'x'):
                canProgramExit = True
                break

        if (isManual):
            while (not(pIsValid) and not(canProgramExit)):
                p = input("Enter a prime modulus (between 1 and 100)\n")
                if p.lower() == 'x':
                    canProgramExit = True
                    break
                elif (isInt(p)):
                    p = int(p)
                    if (p <= 100 and p > 1):
                        if (isPrime(p)):
                            pIsValid = True
                        else:
                            print("Please enter a valid prime number")
                    else:
                        print("The prime modulus must be greater than 1 and less than 100")
                else:
                    print("Please enter a valid prime number")

            while(not(gIsValid) and not(canProgramExit)):
                primitive_roots_list = primitive_roots(p)
                print("Please select one of the following primitive roots for the generator, g:\n",
                    primitive_roots_list)
                g = input()
                if g.lower() == 'x':
                    canProgramExit = True
                    break
                elif (isInt(g)):
                    g = int(g)
                    if (g in primitive_roots_list):
                        gIsValid = True
                    else:
                        print("That is not a valid primitive root of", p)

            while(not(xaIsValid) and not(canProgramExit)):
                xa = input("Enter first private random number\n")
                if xa.lower() == 'x':
                    canProgramExit = True
                    break
                elif (isInt(xa)):
                    xa = int(xa)
                    if (xa > 1 and xa < p ):
                        xaIsValid = True

            while(not(xbIsValid) and not(canProgramExit)):
                xb = input("Enter second private random number\n")
                if xb.lower() == 'x':
                    canProgramExit = True
                    break
                elif (isInt(xb)):
                    xb = int(xb)
                    if (xb > 1 and xb < p ):
                        xbIsValid = True

            if canProgramExit:
                break 

            calculateOutputs(p, g, xa, xb)

        elif (isAuto):
            pIsValid = False
            while (not(pIsValid)):
                p = randomGeneration()
                pIsValid = isPrime(p)

            primitive_roots_list = primitive_roots(p)
            n = randomGeneration(0, len(primitive_roots_list) - 1)
            g = primitive_roots_list[n]
            # 1 < xa < p
            xa = randomGeneration(2, p-1)
            # 1 < xb < p
            xb = randomGeneration(2, p-1)

            print("p: %d\ng: %d\nxa: %d\nxb: %d" % (p, g, xa, xb))

            calculateOutputs(p, g, xa, xb)

main()
