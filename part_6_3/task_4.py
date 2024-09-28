#На вход программе подается одно вещественное число x измеряемое в градусаx
#Программа должна вывести одно число – значение тригонометрического выражения.


from math import *
angle_x = float(input())
angle_x_radians = radians(angle_x)

print(sin(angle_x_radians) + cos(angle_x_radians) + pow(tan(angle_x_radians), 2))