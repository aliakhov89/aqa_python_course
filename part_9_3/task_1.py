#На вход программе подаётся строка, состоящая из имени и фамилии человека, разделённых одним пробелом.
# Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.

#Программа должна вывести «YES», если имя и фамилия начинаются с заглавной буквы, или «NO» в противном случае.

name_surname = input()
if name_surname == name_surname.title():
    print('YES')
else:
    print('NO')

