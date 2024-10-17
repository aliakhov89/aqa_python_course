#На вход программе подается одна строка.
# Напишите программу, которая выводит сообщение «Цифра» (без кавычек), если строка содержит цифру.
# В противном случае вывести сообщение «Цифр нет» (без кавычек).

typed_str = input()
flag = True
for symbol in range(len(typed_str)):
    if typed_str[symbol] in '0123456789':
        print('Digit')
        flag = False
        break
if flag:
    print('No Digits')

