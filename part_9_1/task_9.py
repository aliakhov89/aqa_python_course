#На вход программе подается одна строка.
# Напишите программу, которая определяет сколько в ней одинаковых соседних символов.

typed_symbols = input()
sum_same = 0
for symbol in range(len(typed_symbols) - 1):
    if typed_symbols[symbol] == typed_symbols[symbol + 1]:
        sum_same += 1
print(sum_same)