n = int (input ("Введите значение N: "))
list = []
with open('file (for HW9).txt') as file:
    x = int(file.readline())
    y = int(file.readline())
for i in range(-n,n+1):
    list.append(i)
print (list[x]*list[y])