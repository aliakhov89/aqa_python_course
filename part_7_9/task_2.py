#Дано натуральное число n.
#Напишите программу, которая печатает численный треугольник с высотой равной n, в соответствии с примером:

#1
#121
#12321
#1234321
#123454321
#...

#Примечание. Используйте вложенный цикл for.

typed_nmb = int(input())
for i in range(1, typed_nmb + 1):
    for j in range(i):
        print(j + 1, end = '')
    for k in range(i - 1, 0, -1):
            print(k, end= '')
    print()