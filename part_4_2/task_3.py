#Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанному промежутку от -30 до -2  и от 7 до 25
#На вход программе подаётся целое число x
#Программа должна вывести текст в соответствии с условием задачи.

typed_nmb = int(input())
if -30 < typed_nmb <= -2 or 7 < typed_nmb <= 25 :
    print('Belongs')
else:
    print('Not Belongs')