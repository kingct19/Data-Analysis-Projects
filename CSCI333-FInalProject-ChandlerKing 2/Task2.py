#Task2
#Chandler King
#50260521

import pandas as pd
import matplotlib.pyplot as plt


patients = {}
with open('patientList.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
       name = line[1]
       pain = 2
       patients[name] = int(pain)

patientData = pd.DataFrame(patients, index=['Pain'])

patientData = pd.DataFrame(patients, index=['Pain'], columns=['Name'])

temp_readings = patientData['Name']

pain_readings = patientData.loc['Pain']

level_dict = {0:'No Pain', 1:'Mild', 2:'Mild', 3:'Mild', 4:'Moderate', 5:'Moderate', 6:'Moderate', 7:'Severe', 8:'Severe', 9:'Severe', 10:'Worst'}
patientData['Level'] = patientData['Pain'].apply(lambda x: level_dict[x])

patientData.describe()
patientData.T

level_freq = [0]*5
for i in range(500):
    level_freq[patientData['Level'][i]] += 1

x = ['No Pain', 'Mild', 'Moderate', 'Severe', 'Worst']
y = [level_freq[i]/500 for i in range(5)]

plt.bar(x,y)
plt.xlabel('Pain')
plt.ylabel('Frequency (%)')
plt.title('Statistics')
plt.show()