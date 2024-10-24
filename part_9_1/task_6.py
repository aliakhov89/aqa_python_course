#На вход программе подается одна строка состоящая из цифр.
#Напишите программу, которая считает сумму цифр данной строки.

typed_nmbs = input()
sum = 0
for nmb in range(len(typed_nmbs)):
    sum += int(typed_nmbs[nmb])
print(sum)