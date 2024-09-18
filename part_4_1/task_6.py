#На вход программе подаются два различных целых числа.
#Программа должна вывести наименьшее из двух чисел.

first_digit = int(input())
second_digit = int(input())
if first_digit > second_digit:
    print(second_digit)
else:
    print(first_digit)