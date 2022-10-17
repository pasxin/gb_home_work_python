# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.

import math
list = [2, 3, 11, 5, 6]
resultat = [list [i]*list[-i-1] for i in range (math.ceil (len(list)/2))]
print (resultat)