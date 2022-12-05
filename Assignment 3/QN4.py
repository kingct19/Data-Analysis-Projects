
def smallest(x, y, z):
    result = x
    if y < result:
        result = y
    if z < result:
        result = z
    return result

def average(x, y, z):
    return (x + y + z) / 3


def main():
    x = int(input("Enter Interger: "))
    y = int(input("Enter Interger: "))
    z = int(input("Enter Interger: "))
    print("Smallest Interger: ", smallest(x, y, z))
    print("Avergae Interger: ", average(x, y, z))

if __name__ == '__main__':
    main()