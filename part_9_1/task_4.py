#На вход программе подается одна строка.
# Напишите программу, которая выводит в столбик элементы строки в обратном порядке.

typed_symbols = input()
for symbol in range(-1, - len(typed_symbols) - 1, -1):
    print(typed_symbols[symbol])

#Через зріз
typed_symbols = input()
print(*typed_symbols[::-1], sep = '\n')