#На вход программе подается натуральное число, записанное в десятичной системе счисления.
# Напишите программу, которая переводит данное число в двоичную систему счисления.


typed_nmb = int(input())
remainder_of_division = ''
mirrored_remainder_of_division = ''
while typed_nmb > 0:
    remainder_of_division += str(typed_nmb % 2)
    typed_nmb //= 2
for digit in range(-1, - len(remainder_of_division) -1, -1):
    mirrored_remainder_of_division += remainder_of_division[digit]
print(mirrored_remainder_of_division)