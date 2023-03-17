x = 1
triangle_num = 0

def Check_divisior(x):
    divisors_num = 0
    for i in range (1,(x+1)):
        if x % i == 0:
            divisors_num += 1
    return divisors_num

divisors_num = 0


while divisors_num < 501:
    for i in range (1,x+1):
        triangle_num += i
    divisors_num = Check_divisior(triangle_num)
    triangle_num = 0
    x += 1

print(triangle_num)