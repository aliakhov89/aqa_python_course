#На вход программе подается натуральное число n.
#Напишите программу, которая вычисляет значение выражения

from math import *
num_n = int(input())
total = 0
for i in range(1, num_n + 1):
    total += 1 / i
print(total - log(num_n))