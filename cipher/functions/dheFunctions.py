# === DHE - Diffie-Helman Exchange === #

import random
from math import gcd
import math

def is_primitive_root(g, n):
    """ Find out if g is a primitive root of n """

    # If the greatest common denominator between g and n is NOT 1, then g is not a primtive root 
    if gcd(g, n) != 1:
        return False
    
    # Euler's totient function for n
    totient = n - 1 
    # Define prime numbers as a set
    prime_factors = set()

    # Find the prime factors of Euler's totient
    for i in range(2, int(totient**0.5) + 1):
        # If totient is divisible by number
        while totient % i == 0:
            # Number must be prime
            prime_factors.add(i)
            # reduce totient
            totient //= i
        # stop when totient is 1
        if totient == 1:
            break
    # Totient itself is a prime factor
    if totient > 1:
        prime_factors.add(totient)

    # Go through each prime factor and check if it a primitive root
    for p in prime_factors:
        # if g^(n-1)//p mod n equals 1, then not a primitive root
        if (squareAndMultiply(g, (n - 1) // p, n)) == 1:
            return False

    return True

def primitive_roots(n):
    """ Find all primitive roots of n and put them into a list """
    primitive_roots_list = []
    # 2 has no primitive roots
    if n == 2:
        return primitive_roots_list
    # Go through every numbers between 1 and n and check whether it is 
    # a primitive root of n
    primitive_roots_list = [g for g in range(1, n) if is_primitive_root(g, n)]
    # Return a list of the primitive roots of n
    return primitive_roots_list

def squareAndMultiply(base, exponent, modulus=None):
    """ Square and multiply function to calculate base^(exponent) mod modulus"""
    # Set result to the base number for first 1 bit
    result = base

    # Convert to binary number and remove 0b from result
    binary_exponent = bin(exponent)[2:]

    # Go through every bit within the binary number (starting after the first bit) 
    for index in range(1, len(binary_exponent)):
        # If bit is 1, square and multiply result
        if binary_exponent[index] == "1":
            result = (result * result * base) % modulus if modulus is not None else result * result * base
        # If bit is 0, just square result
        else:
            result = (result * result) % modulus if modulus is not None else result * base
    # Return integer
    return result

def isPrime(p):
    """ Check whether the prime modulus is prime """
    # We don't want 1
    if p <= 1:
        return False
    # 2 is a prime
    if p == 2:
        return True
    # All even numbers (after 2) are not prime
    if p % 2 == 0:
        return False

    # Starting from 3, go through every odd number up until p
    for i in range(3, p, 2):
        # if p is divisible by any number, it cannot be a prime
        if p % i == 0:
            return False
        
    # p is a prime
    return True

def isInt(input):
    """ Check the input is a valid integer"""

    # If value cannot be converted from a string to an integer, it is not valid
    try:
        int(input)
        return True
    except ValueError:
        print("That is not a valid integer")
        return False

def randomGeneration(min=1, max=99):
    """ Randomly generate a number with the [min, max] range"""
    random_int = random.randint(min, max)
    return random_int

def calculateOutputs(p, g, xa, xb):
    """ Calculate ya, yb, k1, and k2 using the square and multiply algorithm """
    # ya = g^xa mod p
    ya = squareAndMultiply(g, xa, p)
    # yb = g^xb mod p
    yb = squareAndMultiply(g, xb, p)
    # one person's private key is yb^xb mod p
    k1 = squareAndMultiply(yb, xa, p)
    # second person' private key is ya^xb mod p
    k2 = squareAndMultiply(ya, xb, p)

    # Printing both private keys to ensure algorithm has been performed correctly
    print("k1:", k1)
    print("k2:", k2)

def main():
    """ Run program and show menu """
    print("Diffie-Helman Exchange Key Algorithm")
    print("Press 'x' to exit program")

    canProgramExit = False

    # While program has not been prompted to quit
    while (not(canProgramExit)):
        pIsValid = False
        gIsValid = False
        xaIsValid = False
        xbIsValid = False

        isAuto = False
        isManual = False
        isSelectionChosen = False

        # Ask user if they want auto or manual input
        while (not(isSelectionChosen)):
            s = input("Do you want to automatically generate inputs (y/n)? ")
            # Auto input
            if (s.lower() == 'y'):
                isAuto = True
                isSelectionChosen = True
            # Manual input
            elif(s.lower() == 'n'):
                isManual = True
                isSelectionChosen = True
            # Quit program
            elif(s.lower() == 'x'):
                canProgramExit = True
                break

        # Manul input chosen 
        if (isManual):
            while (not(pIsValid) and not(canProgramExit)):
                # Prompt user for prime modulus
                p = input("Enter a prime modulus (between 1 and 100)\n")
                if p.lower() == 'x':
                    canProgramExit = True
                    break
                # Check input is an integer
                elif (isInt(p)):
                    p = int(p)
                    # Check valid range of 1 < p <= 100 (we dont want 2 bc it has no primitive roots)
                    if (p <= 100 and p > 2):
                        # Check p is a prime number 
                        if (isPrime(p)):
                            pIsValid = True
                        else:
                            print("Please enter a valid prime number")
                    else:
                        print("The prime modulus must be greater than 1 and less than 100")
                else:
                    print("Please enter a valid prime number")

            while(not(gIsValid) and not(canProgramExit)):
                # Get all primitive roots of p
                primitive_roots_list = primitive_roots(p)
                # Prompt user for a generator
                print("Please select one of the following primitive roots for the generator, g:\n",
                    primitive_roots_list)
                g = input()
                # Quit program
                if g.lower() == 'x':
                    canProgramExit = True
                    break
                # Check g is an integer
                elif (isInt(g)):
                    g = int(g)
                    # Check g lies within the primitive roots list 
                    if (g in primitive_roots_list):
                        gIsValid = True
                    else:
                        print("That is not a valid primitive root of", p)
            
            while(not(xaIsValid) and not(canProgramExit)):
                # Prompt user for xA
                xa = input("Enter first private random number\n")
                if xa.lower() == 'x':
                    canProgramExit = True
                    break
                # Check xA is an integer
                elif (isInt(xa)):
                    xa = int(xa)
                    # Check xA lies within range of 1 < xA < p
                    if (xa > 1 and xa < p ):
                        xaIsValid = True

            while(not(xbIsValid) and not(canProgramExit)):
                # Prompt user for second number xB
                xb = input("Enter second private random number\n")
                if xb.lower() == 'x':
                    canProgramExit = True
                    break
                # Check xB is an integer
                elif (isInt(xb)):
                    xb = int(xb)
                    # Check xB lies within range of 1 < xB < p
                    if (xb > 1 and xb < p ):
                        xbIsValid = True
            # Exit program
            if canProgramExit:
                break 

            # Calculate and print all outputs
            calculateOutputs(p, g, xa, xb)

        # Auto input chosen
        elif (isAuto):
            pIsValid = False
            # Keep randomly generating a number for p until a valid prime number is found
            while (not(pIsValid)):
                p = randomGeneration()
                pIsValid = isPrime(p)
            # Generate all primitive roots of p
            primitive_roots_list = primitive_roots(p)
            # Randomly choose an index within the primitive roots list
            n = randomGeneration(0, len(primitive_roots_list) - 1)
            g = primitive_roots_list[n]
            # Randomly generate a private number xA such that 1 < xA < p
            xa = randomGeneration(2, p-1)
            # Randomly generate a private number xB such that 1 < xB < p
            xb = randomGeneration(2, p-1)
            # Print inputs
            print("p: %d\ng: %d\nxa: %d\nxb: %d" % (p, g, xa, xb))
            # Calculate and print outputs
            calculateOutputs(p, g, xa, xb)

main()
