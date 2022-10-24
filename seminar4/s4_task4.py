#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint
def funk(k):
    file = open('C:\\Users\\annet\\OneDrive\\Рабочий стол\\Python_Task\\seminar4\\file.txt', 'w')
    list = []
    x = int(0)
    for i in range(-k, -1):
        x = randint(1, 101)
        if x !=0:
            file.write(str(x))
            file.write('*x^')
            file.write(str(-i))
            file.write('+')
    x = randint(1, 101)
    if x != 0:
        file.write(str(x))
        file.write('*x+')
    x = randint(1, 101)
    if x != 0:
        file.write('=0')
        file.close()

number = int(input('Введите коэффициент k:'))
funk(number)