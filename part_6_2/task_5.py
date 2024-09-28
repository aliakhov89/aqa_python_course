#Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет,
# можно ли из длин этих строк построить арифметическую прогрессию.
#Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, или «NO» в противном случае.

typed_text_1 = input()
typed_text_2 = input()
typed_text_3 = input()

max_length = max(len(typed_text_1), len(typed_text_2), len(typed_text_3))
min_length = min(len(typed_text_1), len(typed_text_2), len(typed_text_3))
med_length = len(typed_text_1) + len(typed_text_2) + len(typed_text_3) - max_length - min_length

if med_length - min_length == max_length - med_length:
    print('YES')
else:
    print('NO')