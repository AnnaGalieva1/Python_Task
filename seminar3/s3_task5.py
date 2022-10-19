#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число:'))
def fibonacci_list(n):
    fibonacci_numbers = []
    a, b = 1, 1
    for i in range(n):
        fibonacci_numbers.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(0, n + 1):
        fibonacci_numbers.insert(0, a)
        a, b = b, a - b
    return fibonacci_numbers
fibonacci_numbers = fibonacci_list(n)
print(fibonacci_list(n))
