#Даны два целых числа m и n (m≤n).
#Напишите программу, которая выводит все целые числа от m до n (включительно) удовлетворяющие хотя бы одному из условий:
# - число кратно 17
# - число оканчивается на 9
# - число кратно 3 и 5 одновременно

start_nmb, last_nmb = int(input()), int(input())
for i in range(start_nmb, last_nmb + 1):
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif i % 5 == 0 and i % 3 == 0:
        print(i)