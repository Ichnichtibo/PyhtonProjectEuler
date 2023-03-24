import math
a = 1
b = 2
c = a + b
last_number_list = []
list_of_Fibonacci = [1,1,2,3]

while(len(last_number_list) < 1000):
    last_number_list = []
    a = b
    b = c
    c = a+b
    list_of_Fibonacci.append(c)
    for i in str(c):
        last_number_list.append(i)
    print(last_number_list)

print(len(list_of_Fibonacci))
print(c)
print(10**2)
