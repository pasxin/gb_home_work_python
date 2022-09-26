# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# AB = √(AC2 + BC2)
import math
ferst_coordinates = [float (input("Введите значени Х1: ")),float (input("Введите значени Y1: "))]
second_coordinates = [float (input("Введите значени Х2: ")),float (input("Введите значени Y2: "))]
distance = math.sqrt(((second_coordinates [0]-ferst_coordinates[0])**2+(second_coordinates [1]-ferst_coordinates[1])**2))
print ("Растояние межд заданными точками равно: ", '%.2f' % distance)
