#На вход программе подаётся одно целое число – возраст пользователя.
#Программа должна вывести название возрастной группы.

typed_age = int(input())

if typed_age < 14:
    print('childhood')
if 13 < typed_age < 25:
    print('youth')
if 24 < typed_age < 59:
    print('maturity')
if typed_age > 59:
    print('old age')

