#На вход программе подается строка текста в которой буква «h» встречается как минимум два раза.
# Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов, заключенную между первым и последним вхождением буквы «h».

typed_text = input()
first_h = typed_text.find('h')
second_h = typed_text.rfind('h')
print(typed_text[:first_h + 1] + typed_text[second_h - 1:first_h:-1] + typed_text[second_h:])