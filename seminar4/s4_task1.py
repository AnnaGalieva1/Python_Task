#Вычислить число c заданной точностью d.

from math import pi

d =  int(input("Введите число:\n"))
print(f'число Пи с заданной точностью {d} = {round(pi, d)}')