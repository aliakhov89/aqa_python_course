#На вход программе подаются четыре целых числа.
#Программа должна вывести наименьшее из четырёх чисел.

first_digit = int(input())
second_digit = int(input())
third_digit = int(input())
fourth_digit = int(input())

if first_digit < second_digit:
    less_of_first_two = first_digit
else:
    less_of_first_two = second_digit
if third_digit < fourth_digit:
    less_of_other_two = third_digit
else:
    less_of_other_two = fourth_digit
if less_of_other_two < less_of_first_two:
    print(less_of_other_two)
else:
    print(less_of_first_two)
