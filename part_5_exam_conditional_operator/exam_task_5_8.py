#Даны две различные клетки шахматной доски.
#Напишите программу, которая определяет, может ли ферзь попасть с первой клетки на вторую одним ходом.
#Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
#Программа должна вывести «YES», если из первой клетки ходом ферзя можно попасть во вторую, или «NO» в противном случае.

row_1 = int(input())
column_1 = int(input())
row_2 = int(input())
column_2 = int(input())

if row_1 == row_2 or column_1 == column_2:
    print('YES')
elif (row_1 + column_1 == row_2 + column_2) or (row_1 - column_1 == row_2 - column_2):
    print('YES')
else:
    print('NO')