#Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет,
# можно ли из длин этих строк построить арифметическую прогрессию.
#Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, или «NO» в противном случае.

typed_text_1, typed_text_2, typed_text_3 = input(), input(), input()
min_length, med_length, max_length = sorted([len(typed_text_1), len(typed_text_2), len(typed_text_3)])


if med_length - min_length == max_length - med_length:
    print('YES')
else:
    print('NO')