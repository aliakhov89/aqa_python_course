#Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты квадратного уравнения
# ax**2+bx+c=0 и возвращает его корни в порядке возрастания.

#Примечание Гарантируется, что квадратное уравнение имеет хотя бы один корень.
from math import *
def solve(a, b, c):
    discriminant = pow(b, 2) - 4 * a * c
    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)
    return sorted([x1,x2])

a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)
