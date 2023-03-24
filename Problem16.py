n = 2**1000
list1 = []
toplam = 0
for i in str(n):
    list1.append(i)

for i in list1:
    toplam += int(i)

print(toplam)