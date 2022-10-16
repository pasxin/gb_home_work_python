# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# алгоритм сжатия
def alg_RLE (text):
    char = 0
    count = 1
    resultat = ''
    text+= ' '
    for i in range (1,len(text)):
        if char == text[i]:
            count += 1
        else: 
            resultat += str(count) + text [i-1] 
            char = text [i]
            count = 1
    return resultat

# Алг. ре.
def refresh_RLE (text):
    numbers = ''
    resultat = ''
    for i in range (len (text)):
        if '0' <= text [i] <= '9':
            numbers += text [i]
        else:
            resultat += text [i] * int (numbers)
            numbers = '' 
    return resultat

# Основной код
import codecs
print ('1 - сжатие RLE')
print ('2 - Реархивация')
menu = int (input ('Ваш выбор? - '))
if menu == 1:
    with codecs.open ('file_for_HW_24_alg_RLE.txt','r', encoding = 'utf-8') as file:
        text = str (file.readline())
    text = alg_RLE (text)
    with codecs.open ('file_for_HW_24_alg_RLE_result.txt','w', encoding = 'utf-8') as file:
        file.write (text)
elif menu == 2:
    with codecs.open ('file_for_HW_24_refresh_RLE.txt','r', encoding = 'utf-8') as file:
        text = str (file.readline())
    text = refresh_RLE (text)
    with codecs.open ('file_for_HW_24_refresh_RLE_result.txt','w', encoding = 'utf-8') as file:
        file.write (text)
