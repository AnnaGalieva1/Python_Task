#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

print('Введите целое число больше 0:')
number = int(input())
def transformation_in_binary_number(number):
    res = ''
    if number > 0:
        while number != 0:
            res = str(number % 2) + res
            number //= 2
        print(f'Двоичное число: {res}.')
    else: print('Неверный ввод')
transformation_in_binary_number(number)