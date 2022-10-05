# Вычислить число c заданной точностью d
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from cmath import pi
import math


d = int(input ("Введите колличество знаков после запятой: "))
resultat = math.floor(pi) + float ( str (pi % 1)[:2+d])
print(resultat)