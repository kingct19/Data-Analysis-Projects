#Task 1 
#Chandler King
#50260521

import random
from urllib import response
import numpy as np
import statistics
import matplotlib.pyplot as plt


with open('namelist.txt', 'r') as f:
    lines = f.readlines()
    patientlist = lines[5026:5526]

responses = []
for i in range(500):
    responses.append(random.randint(0,10))

with open('patientList.txt', 'w') as f:
    for i in range(500):
        f.write(patientlist[i] + ' ' + str(responses[i]) + '\n')

freq = [0]*11
for i in range(500):
    freq[responses[i]] += 1

min_response = min(responses)
max_response = max(responses)
range_response = max_response - min_response
mean_response = statistics.mean(responses)
median_response = statistics.median(responses)
variance_response = np.var(responses)
std_response = np.std(responses)

x = [0,1,2,3,4,5,6,7,8,9,10]
y = [freq[i]/500 for i in range(11)]

plt.bar(x,y)
plt.ylabel('Frequency (%) ')
plt.title('Response Stats')
plt.show()

for i in range(11):
    print('Pain ' + str(i) + ': ' + str(freq[i]/500))