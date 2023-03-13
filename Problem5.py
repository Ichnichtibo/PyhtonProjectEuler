stopNum = 0
x = 0

while stopNum < 1:
    is_divisible = True
    x += 20
    for i in range(1,20):
        if x % i != 0:
            is_divisible = False

    if is_divisible:
        print(x)
        stopNum += 1