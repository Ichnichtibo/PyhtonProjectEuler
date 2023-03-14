nums = range(1,2000000)

def is_prime(num):
    for x in range (2,num):
        if (num%x) == 0:
            return False
    return True

nums = list(filter(is_prime, nums))

prime_Sum = 0

for i in nums:
    prime_Sum += i

print(prime_Sum)