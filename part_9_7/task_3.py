#На вход программе подается строка текста.
#Напишите программу, которая переводит каждый ее символ в соответствующий ему код из таблицы символов Unicode.


typed_txt = input()
for symbol in typed_txt:
    print(ord(symbol), end = ' ')