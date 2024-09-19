#На вход программе подаются три числа, каждое на отдельной строке.
#Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи.

digit_1 = int(input())
digit_2 = int(input())
digit_3 = int(input())
is_arithmetic_progression = (digit_2 - digit_1) + digit_2
if is_arithmetic_progression == digit_3:
    print('YES')
else:
    print('NO')


