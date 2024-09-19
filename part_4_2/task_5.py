#Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.
#На вход программе подаются три положительных целых числа.
#Программа должна вывести «YES» или «NO» в соответствии с условием задачи.

side_a = int(input())
side_b = int(input())
side_c = int(input())

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print('YES')
else:
    print('NO')
