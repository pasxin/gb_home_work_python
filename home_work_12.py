# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.

import math
list = [2, 3, 4, 5, 6]
resultat = []
for i in range (math.ceil (len(list)/2)):
    resultat.append(list [i]*list[-i-1])
print (resultat)