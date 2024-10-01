#Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет,
# можно ли из длин этих строк построить арифметическую прогрессию.
#Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, или «NO» в противном случае.

typed_text_1, typed_text_2, typed_text_3 = input(), input(), input()

typed_text_1_length = len(typed_text_1)
typed_text_2_length = len(typed_text_2)
typed_text_3_length = len(typed_text_3)

max_length = max(typed_text_1_length, typed_text_2_length, typed_text_3_length)
min_length = min(typed_text_1_length, typed_text_2_length, typed_text_3_length)
med_length = typed_text_1_length + typed_text_2_length + typed_text_3_length - max_length - min_length
if med_length - min_length == max_length - med_length:
    print('YES')
else:
    print('NO')