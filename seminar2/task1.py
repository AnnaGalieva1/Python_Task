#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def func(number):
    sum = 0
    number = number.replace(',','.')
    for symbol in number:
        if symbol != '.':
            sum += int(symbol)
    return sum

if __name__ == "__main__":
    chislo = input('Введите число:')
    summa = func(chislo)
    print(summa)