#На вход программе подается одна строка.
#Напишите программу, которая определяет, сколько раз в строке встречаются символы + и *.

#Пример:
#Символ + встречается 5 раз
#Символ * встречается 2 раз

typed_symbols = input()
sum_plus = 0
sum_star = 0
for symbol in typed_symbols:
    if symbol in '*':
        sum_star += 1
    elif symbol in '+':
        sum_plus += 1
print('Symbol + noticed', sum_plus, 'times')
print('Symbol * noticed', sum_star, 'times')

