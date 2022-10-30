#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на чётной позиции. 
lst = [] 
lst = list(map(int, input('Введите список чисел через пробел: ').split())) 
def summa(lst): 
    Sum = 0
    for i in range(len(lst)): 
        if i % 2 != 0: 
             Sum += lst[i] 
             print(Sum) 
summa(lst) 