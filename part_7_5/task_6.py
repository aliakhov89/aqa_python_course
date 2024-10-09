#Дано натуральное число.
# Напишите программу, которая  определяет, состоит ли указанное число из одинаковых цифр.


nmb = int(input())
last_number = nmb % 10
flag = True
while nmb !=0:
    last_digit = nmb % 10
    if last_number != last_digit:
        flag = False
        break
    nmb //= 10
if flag:
    print('YES')
else:
    print('NO')