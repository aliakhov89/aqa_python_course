#На вход программе подается целое трёхзначное число
#Назовём число интересным, если в нём разность максимальной и минимальной цифры равняется средней по величине цифре.
# Напишите программу, которая определяет, интересное число или нет.
# Если число интересное, следует вывести «Число интересное», иначе – «Число неинтересное».


typed_nmb = int(input())
first_digit = typed_nmb // 100
second_digit = typed_nmb // 10 % 10
third_digit = typed_nmb % 10
if max(first_digit, second_digit, third_digit) - min(first_digit, second_digit, third_digit) == ((first_digit + second_digit + third_digit) - max(first_digit, second_digit, third_digit) - min(first_digit, second_digit, third_digit)):
    print("Interesting digit")
else:
    print("Not Interesting digit")