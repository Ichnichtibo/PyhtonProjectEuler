import string
with open("/Users/saykı/Desktop/p022_names.txt", "r") as f:
    names = f.read()

sozluk = dict()
alfabe = string.ascii_uppercase
harf_değeri  = 1  

for harf in alfabe:
    sozluk[harf] = harf_değeri
    harf_değeri += 1

names = names.split(",")

list.sort(names)

index = 1
toplam = 0

for name in names:
    alt_toplam = 0
    name = name[1:len(name)-1]
    for harf in name:
        alt_toplam += sozluk[harf]
    toplam += (alt_toplam * index)
    index += 1

print(toplam)