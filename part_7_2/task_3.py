#Даны два целых числа m и n (m>n).
#Напишите программу, которая выводит все нечетные целые числа от m до n (включительно) в порядке убывания.

start_nmb, last_nmb = int(input()), int(input())
for i in range(start_nmb, last_nmb - 1, - 1):
    if i % 2 != 0:
        print(i)