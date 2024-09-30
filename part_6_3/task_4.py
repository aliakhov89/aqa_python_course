#На вход программе подается одно вещественное число x измеряемое в градусаx
#Программа должна вывести одно число – значение тригонометрического выражения.


from math import *
angle_x = float(input())
print(sin(radians(angle_x)) + cos(radians(angle_x)) + pow(tan(radians(angle_x)), 2))
