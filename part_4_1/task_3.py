#На вход программе подаётся одно целое положительное четырёхзначное число.
#Программа должна вывести «ДА», если соотношение выполняется, или «НЕТ» — если не выполняется.

four_digits_number = int(input())
digit1 = four_digits_number // 1000
digit2 = four_digits_number // 100 % 10
digit3 = four_digits_number  // 10 % 10
digit4 = four_digits_number // 1 % 10
digit1_plus_digit_4 = digit1 + digit4
digit2_minus_digit_3 = digit2 - digit3
if digit1_plus_digit_4 == digit2_minus_digit_3:
    print('YES')
else:
    print('NO')