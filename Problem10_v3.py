'''Geçen 2 çözümde 10 dakikadan fazla beklememe rağmen sonuş gelmedi bende
 Eratosten kalburu denilen bir yöntemi denicem '''

# all_Nums = list(range(2,2000))
# prime_Nums = []

# def not_prime_check(x):
#     prime_Nums.append(all_Nums[x])
#     delete_Num = all_Nums[x]
#     while delete_Num < all_Nums[-1]:
#         all_Nums.remove(delete_Num)
#         delete_Num += delete_Num
# #? böyle bişey çıktı ilk olarak
# #! eee 2000 den önce dememe rağmen 1000 e kadar yaptı ve 5 in katını silmemiş neden bilmiyorum .
# #! düzeltme sadece 3 ve 2 ' nin katını silmiş 2 ve 3 silince bişey olmamış ama 3 ten sonra...
# index = 0

# while all_Nums[index] < len(all_Nums):
#     not_prime_check(index)
#     index += 1

# #? oldu en azından 3 hariç tüm asal sayıları buldum ama neden 3 yok bilmiyorum

# sum_Prime_Nums = 0

# for i in prime_Nums:
#     sum_Prime_Nums += i

# print(sum_Prime_Nums) 

#? tekrardan yapıcam ben bişeyi yanlış yapmışım

# all_Nums = list(range(2,2000))
# prime_Nums = []

# def Del_nums(x):
#     del_num = all_Nums[x]
#     while del_num <= all_Nums[-1]:
#         all_Nums.remove(del_num)
#         del_num += del_num

# index = 0

# while len(all_Nums) > 0:
#     index = 0
#     while index < len(all_Nums):
#         prime_Nums.append(all_Nums[index])
#         Del_nums(index)
#         index += 1

# print(prime_Nums)

# # zort

