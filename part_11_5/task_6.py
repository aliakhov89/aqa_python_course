#На вход программе подается строка текста и строка-разделитель.
# Напишите программу, которая вставляет указанный разделитель между каждым символом введенной строки текста.


typed_text = input()
typed_divider = input()
print(typed_divider.join(typed_text))

