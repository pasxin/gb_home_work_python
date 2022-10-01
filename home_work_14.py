# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def convert_to_2 (number):
    resultat = ""
    while int(number) >= 1:
        resultat = str (int (number)%2) + resultat
        number = int (number) / 2
    return (resultat)



print (convert_to_2 ("2"))