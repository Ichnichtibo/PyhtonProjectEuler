#? 1'den başlayara n tane sayıyı n*(n+1)/2 olarak toplayabiliriz 

def Triangle_num(x):
    divisiors = []
    triangle_num = int(x*(x+1)/2)

    for i in range (2,(triangle_num+1)):
        if triangle_num % i :
            divisiors.append(i)
    return divisiors,triangle_num
    
def Divisiours_count(y):
    list_divisiors = y
    count_divisiors = 0

    for i in list_divisiors:
        count_divisiors += 1
    
    return count_divisiors

x = 1 
num_count = 0

while num_count < 10:
    list_divisiors,triangle_num = Triangle_num(x)
    num_count = Divisiours_count(list_divisiors)
    x += 1

print(x*(x+1)/2)