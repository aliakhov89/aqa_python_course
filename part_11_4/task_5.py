#На вход программе подается натуральное число n, затем n строк,
# затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

#Примечание. Поиск не должен быть чувствителен к регистру символов.

row_amount = int(input())
rows = []
for row in range(row_amount):
    rows.append(input())
query = input()
for symbol in range(len(rows)):
    if query.lower() in rows[symbol].lower():
        print(rows[symbol])