#На вход программе подается целое трёхзначное число
#Назовём число интересным, если в нём разность максимальной и минимальной цифры равняется средней по величине цифре.
# Напишите программу, которая определяет, интересное число или нет.
# Если число интересное, следует вывести «Число интересное», иначе – «Число неинтересное».


typed_nmb = int(input())
max_digit = max(typed_nmb // 100, typed_nmb // 10 % 10, typed_nmb % 10)
min_digit = min(typed_nmb // 100, typed_nmb // 10 % 10, typed_nmb % 10)
med_digit = (typed_nmb // 100 + typed_nmb // 10 % 10 + typed_nmb % 10) - max_digit - min_digit

if max_digit - min_digit == med_digit:
    print("Interesting digit")
else:
    print("Not Interesting digit")