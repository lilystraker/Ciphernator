#  Diffie-Helman Exchange Key Algorithm

def square_and_multiply(base, exponent, modulus=None):
    result = 1
    
    if modulus is not None:
        base = base % modulus  # Reduce the base if a modulus is provided
        
    while exponent > 0:
        # If the current exponent bit is 1, multiply the result by the base
        if exponent % 2 == 1:
            result = (result * base) % modulus if modulus is not None else result * base
        
        # Square the base and halve the exponent
        base = (base * base) % modulus if modulus is not None else base * base
        exponent //= 2
    
    return result

def isDecimal(input):
    try:
        float(input)
        return True
    except ValueError:
        print("That is not a valid decimal number")
        return False
    
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
            else:
                print()


        if (isManual):
            while (not(pIsValid) and not(canProgramExit)):
                p = input("Enter a prime modulus\n")
                if p.lower() == 'x':
                    canProgramExit = True
                    break
                elif (isDecimal(p)):
                    p = float(p)
                    if (p <= 100 and p > 0):
                        pIsValid = True
                    else:
                        print("The prime modulus must be greater than 0 and less than 101")

            while(not(gIsValid) and not(canProgramExit)):
                g = input("Enter a generator number\n")
                if g.lower() == 'x':
                    canProgramExit = True
                    break
                elif (isDecimal(g)):
                    g = float(g)
                    if (g > 0 and g < p):
                        gIsValid = True
                    else:
                        print("The generator number must be greater than 0 and less than p")
            
            while(not(xaIsValid) and not(canProgramExit)):
                xa = input("Enter first private random number\n")
                if xa.lower() == 'x':
                    canProgramExit = True
                    break
                elif (isDecimal(xa)):
                    xa = float(xa)

            while(not(xbIsValid) and not(canProgramExit)):
                xb = input("Enter second private random number\n")
                if xb.lower() == 'x':
                    canProgramExit = True
                    break
                elif (isDecimal(xb)):
                    xb = float(xb)

            if canProgramExit:
                break 

            ya = square_and_multiply(g, xa, p)
            yb = square_and_multiply(g, xb, p)
            k1 = square_and_multiply(yb, xa, p)
            k2 = square_and_multiply(ya, xb, p)
            print(k1)
            print(k2)


main()
