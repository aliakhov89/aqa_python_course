#Даны два целых числа m и n.
#Напишите программу, которая выводит все целые числа от m до n включительно в порядке возрастания, если m<n,
#или в порядке убывания в противном случае.

start_nmb, last_nmb = int(input()), int(input())
if start_nmb < last_nmb:
    for i in range(start_nmb, last_nmb + 1):
        print(i)
else:
    for i in range(start_nmb, last_nmb - 1, - 1):
        print(i)