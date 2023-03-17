biggesst_chain_num = 0
biggest_repeat_num = 0

for n in range(1000000):
    num = n
    new_repeat_num = 1
    while  num > 1:  
        if num % 2 == 1:
            num = 3*num+1
        else:
            num = num / 2
        new_repeat_num += 1
    if biggest_repeat_num < new_repeat_num:
        biggest_repeat_num = new_repeat_num
        biggesst_chain_num = n



print(biggesst_chain_num)
    
# ? EZ WİN BROOOOOOOO TEKTE