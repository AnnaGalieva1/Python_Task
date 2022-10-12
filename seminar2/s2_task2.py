#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def func(number):
    res = []
    a = 1
    for i in range(1, number + 1):
        a *= i
        res.append(a)
    print(res)

if __name__ == "__main__":
    chislo = int(input('Введите число:'))
    func(chislo)