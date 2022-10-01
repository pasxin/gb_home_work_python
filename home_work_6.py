# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = input("введите значение числа ")
number = number.replace('.', '')
size = len (number)
number = number
result = 0
for count in range (size):
    result = result + int (number [count])
print (result)