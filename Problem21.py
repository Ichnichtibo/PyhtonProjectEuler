def sum_of_proper_division(x):
    sum_division = 0
    for i in range(1,x):
        if x % i == 0:
            sum_division += i
    
    return sum_division

sum_amicable_numbers = 0
amicable_numbers = 0

for i in range (1,10000):
    amicable_numbers = sum_of_proper_division(i)
    if i == sum_of_proper_division(amicable_numbers) and i != amicable_numbers:
        sum_amicable_numbers += i

print(sum_amicable_numbers)
