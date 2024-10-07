#Дано натуральное число n(n>9).
# Напишите программу, которая определяет его вторую (с начала) цифру.

num = int(input())
while num >= 10:
    last_number = num % 10
    num //= 10
print(last_number)
