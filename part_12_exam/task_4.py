#На вход программе подается строка текста.
# Напишите программу, которая определяет, является ли введенная строка корректным телефонным номером.
# Строка текста является корректным телефонным номером, если она имеет формат:
#abc-def-hijk или
#7-abc-def-hijk,
#где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.

#Формат входных данных
#На вход программе подается строка текста.
#Формат выходных данных
#Программа должна вывести «YES», если строка является корректным телефонным номером и «NO» в противном случае.
#Примечание. Телефонный номер должен содержать только цифры и символ -, а количество цифр в каждой группе должно быть правильным.

typed_text = [i for i in input().split('-')]
lenth_typed_text = [len(j) for j in typed_text]
if ''.join(typed_text).isdigit() and lenth_typed_text == [3, 3, 4]:
    print('YES')
elif ''.join(typed_text).isdigit() and lenth_typed_text == [1, 3, 3, 4] and typed_text[0] == '7':
    print('YES')
else:
    print('NO')

#In one if:

typed_text = [i for i in input().split('-')]
lenth_typed_text = [len(j) for j in typed_text]
if ''.join(typed_text).isdigit() and (lenth_typed_text == [3, 3, 4] or (lenth_typed_text == [1, 3, 3, 4] and typed_text[0] == '7')):
    print('YES')
else:
    print('NO')