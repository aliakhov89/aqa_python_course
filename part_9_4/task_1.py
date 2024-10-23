#На вход программе подаётся строка текста, состоящая из слов, разделённых ровно одним пробелом.
# Напишите программу, которая подсчитывает количество слов в ней.

typed_text = input()
spaces_amount = typed_text.count(' ')
words_amount = spaces_amount + 1
print(words_amount)