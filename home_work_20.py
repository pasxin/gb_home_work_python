#Даны два файла (file_1_for_HW_20 и file_2_for_HW_20), в каждом из которых находится запись многочлена. 
#Задача - сформировать файл, содержащий сумму многочленов.

def filter (text):
    list = text.split (' + ')
    for i in range (len (list)):
        text = list [i]
        if '0' <= text [0] <= '9':
            char = text [0]
            if len (text) > 1:
                j = 1 
                while '0' <= text [j] <= '9':
                    char += text [j]
                    j += 1            
            list [i] = char
        else: list [i] = 0   
    return list

with open('file_1_for_HW_20.txt') as file:
    ferst = str (file.readline())

with open('file_2_for_HW_20.txt') as file:
    second = str (file.readline())

ferst = filter (ferst)
second = filter (second)
resultat = []
for i in range (len (ferst)):
    resultat.append (int(ferst [i]) + int(second[i]))


data = open ('file_result_for_HW_20.txt','w')
for i in range (len(ferst)-1):    
    data.write (str(resultat[i]) + '*x^'+str (len(ferst) - i - 1) + ' + ')
data.write (str(resultat[len(ferst)-1]))
data.close()
