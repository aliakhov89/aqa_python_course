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

#без флагу
typed_txt = input()
for symbol in typed_txt:
    if symbol in '01234567890':
        print("Digit")
        break
else:
    print("No Digits")