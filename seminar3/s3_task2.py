#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = [1, 5, 4, 2, 7, 9]

if len(list)%2 == 0:
     size = len(list) // 2
import math 
size = math.ceil(len(list)/2)
print(size)
list_2 = []
for i in range(size):
    list_2.append(list[i]*list[-i - 1])
print(list_2)