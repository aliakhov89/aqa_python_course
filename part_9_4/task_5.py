# На вход программе подается строка текста.
# Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.

#Программа должна вывести «YES», если введённая строка заканчивается подстрокой .com или .ru, или «NO» в противном случае.

typed_text = input()
if typed_text.endswith('.com') or typed_text.endswith('.ru'):
    print('YES')
else:
    print('NO')

