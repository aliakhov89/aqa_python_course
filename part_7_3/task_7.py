#На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.

num_n = int(input())
total = 0
for i in range(1, num_n + 1):
    if num_n % i == 0:
        total += i
print(total)