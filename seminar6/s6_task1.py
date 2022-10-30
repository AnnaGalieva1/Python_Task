#предложить улучшения кода для уже решённых задач с помощью использования лямбд, filter, map, zip, enumerate, list comprehension
#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму нечетных элементов списка.

def where(f,col):
    return [x for x in col if f(x)]
data = [x for x in range(7)]
print(data)
res = filter(int, data)
res = where(lambda x: x % 2 == 1, res)
res = list(filter(lambda x: x % 2 == 1, res))
print (res)

sum = 0
x = data
for i in range(len(x)):
    if i % 2 == 1: 
        sum += x[i]  
     
print(f"{x} -> сумма нечетных элементов: {sum}")
