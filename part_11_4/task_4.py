#На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.
#Примечание. Считайте, что все строки состоят из строчных символов.

row_amount = int(input())
uniq_rows = []
for row in range(row_amount):
    typed_row = input()
    if typed_row not in uniq_rows:
        uniq_rows.append(typed_row)
print(*uniq_rows, sep='\n')

