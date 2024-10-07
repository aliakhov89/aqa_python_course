#На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет n!. - факториал

num_n = int(input())
total = 1
for i in range(1, num_n + 1):
    total *= i
print(total)

