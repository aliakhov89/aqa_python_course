#На вход программе подается строка.
# Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
#Программа должна вывести количество буквенных символов в нижнем регистре.

typed_text = input()
typed_text_up = typed_text.upper()
symbols_counter = 0
for symbol in range(len(typed_text)):
    if typed_text[symbol] != typed_text_up[symbol]:
        symbols_counter += 1
print(symbols_counter)
