prime_Sum = 0
x = 3

    

while x < 2000000:
    is_prime = True

    for i in range (2,x):
        if x % i == 0:
            is_prime = False

    if is_prime:
        prime_Sum += x
    x += 1

print(prime_Sum)