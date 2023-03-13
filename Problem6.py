sumSquare = 0
squareSum = 0

for i in range (101):
    squareSum += i**2
    

for j in range (101):
    sumSquare += j

print((sumSquare ** 2) - (squareSum)) 