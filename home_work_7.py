# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
result = 1
list = []
size = int (input("введите диапазон "))
for i in range (1,size+1):
    result *= i
    list.append(result)
print (list)