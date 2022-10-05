# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.


number = int (input ("Введите натуральное число N: "))
resultat = []
while number % 2 == 0 or number % 3 == 0:
    if number % 2 == 0:
        resultat.append (2)
        number /= 2
    elif number % 3 == 0:
        resultat.append (3)
        number /= 3
resultat.append (int (number))
print (resultat)
