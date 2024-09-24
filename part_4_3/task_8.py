#На вход программе подаётся одно целое число.
#Программа должна вывести цвет кармана либо сообщение «ошибка ввода»,
# если введённое число лежит вне диапазона от 0 до 36.

input_nmb = int(input())
if input_nmb < 0 or input_nmb > 36:
    print('input error')
elif input_nmb == 0:
    print('green')
elif 1 <= input_nmb <= 10:
    if input_nmb % 2 == 0:
        print('black')
    else:
        print('red')
elif 11 <= input_nmb <= 18:
    if input_nmb % 2 == 0:
        print('red')
    else:
        print('black')
elif 19 <= input_nmb <= 28:
    if input_nmb % 2 == 0:
        print('black')
    else:
        print('red')
elif 29 <= input_nmb <= 36:
    if input_nmb % 2 == 0:
        print('red')
    else:
        print('black')