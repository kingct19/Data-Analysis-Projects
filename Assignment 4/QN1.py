

values=[]

for i in range(1,11):
    values.append(i)

for i in range(0,21,2):
    values.append(i)

for i in range(1,11):
    values.append(i*i)

for i in range(1,11):
    values.append(0)

values=values+[1,4,9,16,9,7,4,9,11]

values=values+[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

for i in range(0,2):
    for j in range(0,5):
        values.append(j)

print(values)