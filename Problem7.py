prime_number = 1
x = 3

# def check_prime(x):
#     is_prime = True

#     for i in range (2,x):
#         if x % i == 0:
#             is_prime = False

#     if is_prime:
#         print(x)
        

while prime_number < 10002:
    is_prime = True

    for i in range (2,x):
        if x % i == 0:
            is_prime = False

    if is_prime:
        print(x)
        prime_number += 1
    x += 1
