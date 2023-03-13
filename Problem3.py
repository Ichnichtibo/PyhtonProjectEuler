import math

def prime_check(x):
    is_prime = True

    for num in range (2,x):
        if x % num == 0:
            is_prime = False
    if is_prime:
        print(x)

for i in range (2,600851475143):
    if 600851475143 % i == 0:
        prime_check(i)
