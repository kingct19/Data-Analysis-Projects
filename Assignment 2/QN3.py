

import random

random_numbers = []
for num in range(100):
    random_numbers.append(random.randint(1,1000))

odd_values = 0
for num in random_numbers:
    if (num % 2 !=0):
        odd_values += 1

even_values = 100 - odd_values

print("There are", even_values, "Even numbers and", odd_values, "Odd Numbers.")