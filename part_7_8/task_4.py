#Дано нечетное натуральное число n.
#Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным n в соответствии с примером:

#*
#**
#***
#****
#***
#**
#*

#На вход программе подается одно нечетное натуральное число.
#Программа должна вывести треугольник в соответствии с условием.

typed_nmb = int(input())
for i in range(1, typed_nmb + 1):
    print('*' * min(i, typed_nmb - i + 1))
