#На вход программе подаётся натуральное число n(n≥2) – катет прямоугольного равнобедренного треугольника.
#Напишите программу, которая выводит звёздный треугольник в соответствии с примером.

stars_qty = int(input())
for i in range(stars_qty):
    print(stars_qty * '*')
    stars_qty = stars_qty - 1