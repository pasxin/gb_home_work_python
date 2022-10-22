import codecs


# добавляет текст на новую строку
def txt_add_line (text):   
    with codecs.open ('file_for_HW_27_line.txt','a', encoding = 'utf-8') as file:
        file.write (' '.join(text)+"\n")

def txt_add (text):   
    with codecs.open ('file_for_HW_27.txt','a', encoding = 'utf-8') as file:
        file.write (text[0]+"\n"+text[1]+"\n"+text[2]+"\n"+text[3]+'\n')
        
def csv_add_line (text):   
    with codecs.open ('file_for_HW_27_line.csv','a', encoding = 'utf-8') as file:
        file.write (text[0]+"-"+text[1]+"-"+text[2]+"-"+text[3]+"\n")

def csv_add (text):   
    with codecs.open ('file_for_HW_27.csv','a', encoding = 'utf-8') as file:
        file.write (text[0]+","+text[1]+","+text[2]+","+text[3]+'\n')

#читает все строки
def txt_reader (f):
    resultat = ''
    with codecs.open (f,'r', encoding = 'utf-8') as file:
        while True:
            text = str (file.readline())
            resultat +=text 
            if not text:
                break
    return resultat
