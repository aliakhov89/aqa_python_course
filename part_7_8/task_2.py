#Дано натуральное число n (n≤ 9).
# Напишите программу, которая печатает таблицу размером n×5, где в i-ой строке указано число i (числа отделены одним пробелом).

#На вход программе подается одно натуральное число.
#Программа должна вывести таблицу размером n×5 в соответствии с условием.

typed_nmb = int(input())
for row in range(1, typed_nmb + 1):
    for column in range(5):
        print(row, end = ' ')
    print()