#Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

total = 1
for i in range(10):
    num_n = int(input())
    if num_n != 0:
        total *= num_n
print(total)
