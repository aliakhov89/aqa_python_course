#На вход программе подается натуральное число n.
#Напишите программу, которая печатает звездный прямоугольник размерами nx19
#На вход программе подаётся натуральное число n∈[1;20] — высота звездного прямоугольника.
#Программа должна вывести звездный прямоугольник размерами n×19.

typed_n = int(input())
for i in range(typed_n):
    print('*******************')