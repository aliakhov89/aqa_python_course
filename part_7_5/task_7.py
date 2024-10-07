#Дано натуральное число.
# Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

nmb = int(input())
flag = True
while nmb >=10:
    last_digit = nmb % 10
    before_last_digit = nmb % 100 // 10
    if last_digit > before_last_digit:
        flag = False
        break
    nmb //= 10
if flag:
    print('YES')
else:
    print('NO')