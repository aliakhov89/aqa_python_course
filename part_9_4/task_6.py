#На вход программе подаётся строка текста.
# Напишите программу, которая выводит на экран символ, который появляется наиболее часто.

#Примечание 1. Если таких символов несколько, следует вывести последний по порядку символ.
#Примечание 2. Следует различать заглавные и строчные буквы, а также буквы русского и английского алфавита.

typed_text = input()
most_often_symbol = ''
most_often_symbol_counter = 0
for symbol in range(len(typed_text)):
    symbol_counter = typed_text.count(typed_text[symbol])
    if symbol_counter >= most_often_symbol_counter:
        most_often_symbol_counter = symbol_counter
        most_often_symbol = typed_text[symbol]
print(most_often_symbol)


