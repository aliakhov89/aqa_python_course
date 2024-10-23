#На вход программе подается строка текста.
#Напишите программу, которая подсчитывает количество цифр в данной строке.

typed_text = input()
digit_counter = 0
for digit in range(0, 10):
    digit_counter += typed_text.count(str(digit))
print(digit_counter)



