import math

n = math.factorial(100)
list1 = []
sumN = 0


print(n)

for i in str(n):
    list1.append(i)

for i in list1:
    sumN += int(i)

print(sumN)
