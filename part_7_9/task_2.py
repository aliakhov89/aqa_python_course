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
for row in range(1, typed_nmb + 1):
    for row_items_increase in range(row):
        print(row_items_increase + 1, end = '')
    for row_items_decrease in range(row - 1, 0, -1):
            print(row_items_decrease, end= '')
    print()