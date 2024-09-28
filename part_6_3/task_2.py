
#Напишите программу, определяющую площадь круга и длину окружности по заданному радиусу R
#На вход программе подаётся одно действительное число R
#Программа должна вывести два числа (каждое на новой строке) – площадь круга и длину окружности радиуса R

import math
radius = float(input())
circle_area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius
print(circle_area, circumference, sep='\n')

