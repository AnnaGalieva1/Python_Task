#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите число: "))
i = 2 # первое простое число
list = []
a = number
while i <= number:
    if number % i == 0:
        list.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {a}: {list}")