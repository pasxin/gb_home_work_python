# Реализуйте алгоритм перемешивания списка (метод random.shuffle использовать нельзя, 
# но другие методы из библиотеки random - можно).
import random
list = [i for i in range (10)]
size = len (list)
for count in range (size):
    position = random.randint (0,size-1)
    memory = list [position]
    list [position] = list [count]
    list [count] = memory
print (list)
