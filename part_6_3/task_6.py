#На вход программе подаются три действительных числа a ≠ 0, b, c, каждое на отдельной строке.

#Программа должна вывести действительные числа – корни уравнения,
# каждый на отдельной строке, если они существуют, или текст «Нет корней» в противном случае.
#Если уравнение имеет два корня, то следует вывести их в порядке возрастания.

from math import *

nmb_a = float(input())
nmb_b = float(input())
nmb_c = float(input())

discriminant = pow(nmb_b, 2) - 4 * nmb_a * nmb_c
if discriminant > 0:
    x_1 = (-nmb_b - sqrt(discriminant)) / (2 * nmb_a)
    x_2 = (-nmb_b + sqrt(discriminant)) / (2 * nmb_a)
    print(min(x_1, x_2))
    print(max(x_1, x_2))
elif discriminant == 0:
    print(-nmb_b / (2 * nmb_a))
else:
    print('no roots')

