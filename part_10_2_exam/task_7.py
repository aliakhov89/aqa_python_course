#На вход программе подается строка текста.
# Напишите программу, которая удаляет из нее все символы с индексами, кратными 3, то есть символы с индексами 0, 3, 6, ....

typed_text = input()
for symbol in range(len(typed_text)):
    if symbol % 3 != 0:
        print(typed_text[symbol], end='')