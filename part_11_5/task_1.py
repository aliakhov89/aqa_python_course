#На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.

words = input().split()
print(*words, sep = '\n')