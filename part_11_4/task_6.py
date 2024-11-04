#На вход программе подается натуральное число n, затем n строк,
# затем число k — количество поисковых запросов, затем k строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки, в которых встречаются одновременно все поисковые запросы.

#Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.
#Примечание. Поиск не должен быть чувствителен к регистру символов.

row_amount = int(input())
rows = []
queries = []
counter = 0
for row in range(row_amount):
    rows.append(input())
k = int(input())
for query in range(k):
    queries.append(input())
for i in range(row_amount):
    for q in range(k):
        if queries[q].lower() in rows[i].lower():
            counter += 1
    if counter == k:
        print(rows[i])
    counter = 0



#with all
row_amount = int(input())
rows = [input() for i in range(row_amount)]
k = int(input())
queries = [input().lower() for j in range(k)]
for row in rows:
    if all(query in row.lower() for query in queries):
        print(row)


