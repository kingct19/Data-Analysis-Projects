#Chandler King Assignment 2 Python
#50260521 


#Problem 1
import math;
import os;

n = int(input("\nEnter a Number: "))

sq = []
i = 0
while(True):
    if( i**2 < n ):
        sq.append(i**2)
    else:
        break
    i += 1
print("\nAll square roots less than n.\n",sq)

div = []
i = 1
while(True):
    if( i*10 < n ):
        div.append(i*10)
    else:
        break
    i += 1
print("\nAll Positive numbers divisible by 10.\n",div)

po = []
i = 0
while(True):
    if( 2**i < n ):
        po.append( 2**i)
    else:
        break
    i += 1
print("\nAll powers of two less than n.\n",po)