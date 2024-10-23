#На вход программе подается строка.
# Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
#Программа должна вывести количество буквенных символов в нижнем регистре.




typed_text = input()
symbols_counter = 0
for symbol in typed_text:
    if symbol != symbol.upper():
        symbols_counter += 1
print(symbols_counter)