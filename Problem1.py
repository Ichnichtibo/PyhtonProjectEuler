numSum = 0

for num in range(1,1000):
    if num % 5 == 0 or num % 3 == 0:
        numSum += num
print(numSum)