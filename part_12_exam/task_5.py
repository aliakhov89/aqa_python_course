#На вход программе подается строка текста.
# Напишите программу, использующую списочное выражение, которая находит длину самого длинного слова.

#Формат входных данных
# На вход программе подается строка текста.

#Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

print(max([len(i) for i in input().split()]))