
import re


def allTheSame(x, y, z):
    if x == y and x == z:
        return True
    else:
        return False

def allDifferent(x, y, z):
    if x != y and x != z and y != z:
        return True
    else:
        return False

def sortedNumber(x, y, z):
    if x > y and y > z:
        return True
    elif x > z and z > y:
        return True
    elif y > x and x > z:
        return True
    elif y > z and z > x:
        return True
    elif z > x and x > y:
        return True
    elif z > y and y > x:
        return True
    else:
        return False

def main():
    x = int(input("Enter Interger: "))
    y = int(input("Enter Interger: "))
    z = int(input("Enter Interger: "))

    print("AllSame Intergers: ", allTheSame(x, y, z))
    print("AllDifferent Intergers: ", allDifferent(x, y, z))
    print("Sorted Intergers: ", sortedNumber(x, y, z))

    
main()