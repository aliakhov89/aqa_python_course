#На вход программе подается строка текста.
# Напишите программу, которая выводит индекс второго вхождения буквы «f».
# Если буква «f» встречается только один раз, выведите число −1, а если не встречается ни разу, выведите число −2.

typed_text = input()
if typed_text.count('f') == 0:
    print(-2)
elif typed_text.count('f') == 1:
    print(-1)
else:
    print(typed_text.find('f', typed_text.find('f') + 1, len(typed_text)))