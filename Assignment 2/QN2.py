

# Generate numbers between 2 to 100
def sumEven():
    sum = 0
    for i in range (2,101,2):
        sum+=i
    return sum

def sumSquares():
    sum = 0 
    for i in range (1, 101):
        sum = sum + (i * i)
    return sum

def sumBetween(a,b):
    sum = 0
    for i in range(a,b+1):
        if i %2 is not 0:
            sum = sum + i
    return sum

def sumOddDigit(num):
    sum = 0
    while num > 0:
        rem = num % 10
        if rem %2 is not 0:
            sum = sum + rem
        num = num // 10
    return sum

print("The Even sum is: ",sumEven())
print("The Squares Sum is: ",sumSquares())
print("The Between Sum is: ",sumBetween(20,100))
print("The Odd digit Sum is: ", sumOddDigit(50000))