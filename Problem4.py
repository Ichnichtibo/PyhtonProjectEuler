def check_palidrom(x):
    is_palidrom = True

    list1 = []
    list2 = []

    for i in str(x):
        list1.append(i)

    for y in str(x)[::-1]:
        list2.append(y)

    if list1 == list2:
        print(list1)
        

for i in range(100,999):
    for y in range(100,999):
        x = i * y
        check_palidrom(x)