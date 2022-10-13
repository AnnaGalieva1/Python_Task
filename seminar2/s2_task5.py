#Реализуйте алгоритм перемешивания списка.

from random import randint

def func(N):
    lst = [3,6,2,9,10,5,1,4,8,7]
    res = []
    for i in range(len(lst)):
        index = randint(0, len(lst) - 1)
        res.append(lst[index])
        lst.remove(lst[index])
    print(res)

if __name__ == "__main__":
    chislo = int(input("Введите число:"))
    func(chislo)
