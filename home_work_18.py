# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

list = [1, 2, 1, 3, 2, 4, 5]
resultat = [list [0]]
for i in range (1,len (list)):
    if list [i] not in resultat:
        resultat.append (list[i])
print (resultat)