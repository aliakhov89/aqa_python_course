#На вход программе подаётся одна строка с буквами русского языка.
#Напишите программу, которая определяет количество гласных и согласных букв и выводит текст в следующем формате:
#Количество гласных букв равно <кол-во гласных букв>
#Количество согласных букв равно <кол-во согласных букв>

# 6 букв могут обозначать vowels: «A», «E», «I», «O», «U», «Y»;
# 21 буква может обозначать consonant:
# «B», «C», «D», «F», «G», «H», «J», «K», «L», «M», «N», «P», «Q», «R», «S», «T», «V», «W», «X», «Y», «Z».

typed_symbols = input()
sum_vowels = 0
sum_consonants = 0
for symbol in range(len(typed_symbols)):
    if typed_symbols[symbol] in 'aeiouyAEIOUY':
        sum_vowels += 1
    elif typed_symbols[symbol] in 'bcdfghjklmnpqrstuvwxyzACDFGHJKLMNPQRSTVWXYZ':
        sum_consonants += 1
print('Amount of vowels is equal', sum_vowels)
print('Amount of consonants is equal', sum_consonants)