# print(6*(9**4))
# 32805

# list_sum_of_fourth_powers = []

# def check_sum_of_fourth_powers(x):
#     check_x = 0
#     for i in str(x):
#         check_x += int(i)**4
#     if check_x == x:
#         list_sum_of_fourth_powers.append(x)

# for x in range(2,32805):
#     check_sum_of_fourth_powers(x)
# print(list_sum_of_fourth_powers)
# !! siktim attım soruyu

# print(6*(9**5))
# 354294

list_sum_of_fifth_powers = []
def check_sum_of_fifth_powers(x):
    check_x = 0
    for i in str(x):  
        check_x += int(i)**5
    if check_x == x:
        list_sum_of_fifth_powers.append(x)

for x in range(2,354294):
    check_sum_of_fifth_powers(x)

just_sum = 0
for i in list_sum_of_fifth_powers:
    just_sum += i

print(just_sum)