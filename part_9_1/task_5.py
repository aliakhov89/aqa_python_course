#На вход программе подаются три строки: имя, фамилия и отчество (именно в таком порядке).
# Напишите программу, которая выводит инициалы человека.

first_name, last_name, patronymic = input(), input(), input()
print(last_name[0] + first_name[0] + patronymic[0])
