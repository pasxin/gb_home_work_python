# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = int (input ("Укажите колличество (значение должно быть больше 1): "))
coefficient = []
for i in range (k):
    coefficient.append (random.randint (0,100))


data = open ('file_for_HW_19.txt','w')
for i in range (k-1):
    if coefficient[i] != 0:
        data.write (str (coefficient[i]) + 'x^'+ str (k - i - 1) + ' + ')
if coefficient[i-1] != 0:
    data.write (str(coefficient[i-1]))
data.write (' = 0')
data.close()
