# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int (input("введите диапазон "))
x = [(1+1/i)**i for i in range (1,n+1)]
print ('%.2f' % sum(x))