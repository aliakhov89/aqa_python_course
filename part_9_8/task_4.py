#На вход программе подаются 2 строки.
# Вам необходимо сравнить эти строки посимвольно, не учитывая регистр и игнорируя все небуквенные символы.
# Программа должна вывести «YES», если строки окажутся равны в результате такой проверки, или «NO» в противном случае.

#Формат входных данных
#На вход программе подаются 2 строки, каждая на отдельной строке.

#Формат выходных данных
# Программа должна вывести «YES» или «NO» в соответствии с условием задачи.


first_row, second_row = input(), input()
first_row_only_letters = ''
second_row_only_letters = ''

for symbol in first_row:
    if symbol.isalpha():
        first_row_only_letters += symbol
for symbol in second_row:
    if symbol.isalpha():
        second_row_only_letters += symbol

if first_row_only_letters.lower() == second_row_only_letters.lower():
    print('YES')
else:
    print('NO')