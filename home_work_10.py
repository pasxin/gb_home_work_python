# Реализуйте алгоритм перемешивания списка (метод random.shuffle использовать нельзя, 
# но другие методы из библиотеки random - можно).
import random
list = [0,1,2,3,4,5,6,7,8,9]
size = len (list) - 1
for count in range (size):
    position = random.randint (0,size)
    memory = list [position]
    list [position] = list [count]
    list [count] = memory
print (list)
