list_numbers = []
def check_list(x):
    check = True
    for i in list_numbers:
        if i == x:
            check = False
    if check:
        list_numbers.append(x)

for i in range(2,101):
    for y in range(2,101):
        x = i**y
        check_list(x)


print(len(list_numbers))
    