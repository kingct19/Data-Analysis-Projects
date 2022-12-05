

gradeCounts={'A':8, 'D':3, 'B':15, 'F':2, 'C':6}

print("Keys: ")
for i in gradeCounts:
    print(i,end=" ")

print("\n\nValues: ")
for i in gradeCounts:
    print(gradeCounts.get(i), end=" ")

print("\n\nKey and Value Pairs: ")
for i,j in gradeCounts.items():
    print((i,j), end=" ")

print("\n\nKey and Value Pairs after sorting keys: ")
for i in sorted(gradeCounts):
    print((i, gradeCounts[i]), end=" ")


print("\n\nThe Average: ")
Avg= 0
for val in gradeCounts.values():
    Avg += val
Avg = Avg / len(gradeCounts)
print(Avg)

print("\n\nChart of astreiks")
str="*"
for i in sorted(gradeCounts):
    print(i,":",str * gradeCounts[i])