#На вход программе подаётся одно целое число – возраст пользователя.
#Программа должна вывести название возрастной группы.

typed_age = int(input())
print('old age' if typed_age > 59 else
      'maturity' if typed_age > 24 else
      'youth' if typed_age > 13 else
      'childhood')



