#Дано натуральное число n(n>99). Напишите программу, которая определяет его третью (с начала) цифру.

typed_nmb = int(input())
while typed_nmb > 999:
    typed_nmb //= 10
print(typed_nmb % 10)