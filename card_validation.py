"""This program implements two functions (is_valid_CC and is_valid_RN)
and test code."""

def is_valid_CC(x):
    
    """This function prompts for a credit card number, prints a statement
     whether it is valid, and prompt for another credit card number"""

    y = x[:-1]
    i = 0
    s = 0
    a = 0
    b = 0
    c = 0
    
    if (len(x) in range(13,17)) and (x[0] == "4" or x[0] == "5" or x[0] == "6" or (x[0] == "3" and x[1] == "7")):
        for i in x[::-2]:
            s += int(i)
        for a in y[::-2]:
            if int(a)*2 // 10 == 0:
                b = int(a)*2
            if int(a)*2 // 10 != 0:
                b = int(a)*2 // 10 + int(a)*2 % 10
            c += b

        if (c+s) % 10 == 0:
            return True
    return False

def is_valid_RN(x):

    """This function prompts for a routing number, prints a statement
     whether it is valid, and prompt for another routing number"""

    i = 0
    s = 0
    a = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0

    y = x[:-1]
    z = x[:-2]

    if len(x) == 9:
        for i in x[::-3]:
            s += int(i)
        for a in y[::-3]:
            c += int(a)
            d = c*7
        for e in z[::-3]:
            f += int(e)
            g = f*3
        if (s+d+g) % 10 == 0:
            return True

        
    return False

if __name__ == "__main__":
    ccn = 0
    while ccn != "q":
        ccn = input("Enter credit card number: ")
        if ccn == "q":
            break
        if is_valid_CC(ccn):
            print(ccn ,"is valid")
        else:
            print(ccn ,"is invalid")

    rn = 0
    while rn != "q":
        rn = input("Enter routing number: ")
        if rn == "q":
            break
        if is_valid_RN(rn):
            print(rn ,"is valid")
        else:
            print(rn ,"is invalid")
        
