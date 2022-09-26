# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = bool(eval(input("Введите значение Х: ")))
y = bool(eval(input("Введите значение Y: ")))
z = bool(eval(input("Введите значение Z: ")))
if not (x or y or z) == (not x) and (not y) and (not z):
    print ("True")
else:
    print ("False")