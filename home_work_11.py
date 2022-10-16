# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = [i for i in range (10,20)]
list_neg = [list [i] for i in range (1,len (list),2)]
print (sum(list_neg))