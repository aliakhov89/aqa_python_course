#Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру.
#Если число находится вне диапазона 1 - 10 то программа должна вывести текст «ошибка».
#На вход программе подаётся целое число.
#Программа должна вывести текст в соответствии с условием задачи.

typed_nmb = int(input())
if typed_nmb == 1:
    print('I')
elif typed_nmb == 2:
    print('II')
elif typed_nmb == 3:
    print('III')
elif typed_nmb == 4:
    print('IV')
elif typed_nmb == 5:
    print('V')
elif typed_nmb == 6:
    print('VI')
elif typed_nmb == 7:
    print('VII')
elif typed_nmb == 8:
    print('VIII')
elif typed_nmb == 9:
    print('IX')
elif typed_nmb == 10:
    print('X')
else:
    print('error')