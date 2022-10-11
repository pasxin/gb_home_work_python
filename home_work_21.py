#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#Входные и выходные данные хранятся в отдельных текстовых файлах.

import codecs

with codecs.open ('file_for_HW_21.txt','r', encoding = 'utf-8') as file:
    text = str (file.readline())

data = codecs.open ('file_result_for_HW_21.txt','w', encoding ='utf-8')
text = list (filter (lambda x: ('абв' not in x), text.split()))
data.write ((' '.join(text)))
data.close()