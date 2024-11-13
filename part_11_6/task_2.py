#На вход программе подается строка текста, содержащая различные натуральные числа.
# Вам необходимо переставить максимальный и минимальный элементы местами и вывести измененную строку.

#На вход программе подается строка текста, содержащая различные натуральные числа, разделенные символом пробела.
#Программа должна вывести текст в соответствии с условием задачи.

#Примечание. Используйте подходящие встроенные функции и списочные методы.

typed_text = input().split()
str_to_int = []
for i in typed_text:
    str_to_int.append(int(i))
index_of_max_digit = str_to_int.index(max(str_to_int))
index_of_min_digit = str_to_int.index(min(str_to_int))
str_to_int[index_of_max_digit], str_to_int[index_of_min_digit] = str_to_int[index_of_min_digit], str_to_int[index_of_max_digit]
print(*str_to_int)