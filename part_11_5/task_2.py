#На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.
# Напишите программу, которая выводит инициалы человека.

typed_name = input().split()
name_parts = []
for i in typed_name:
    name_parts.append(i[0] + '.')
print(''.join(name_parts))


typed_name = input().split()
print(''.join(i[0] + '.' for i in typed_name))