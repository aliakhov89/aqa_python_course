#Дано натуральное число n.
# Напишите программу, которая выводит значение суммы:1!+2!+3!+…+n!
from math import factorial

#Примечание: Задачу можно решить без вложенного цикла. Напишите две версии программы

#1
typed_nmb = int(input())
one_item_fact = 1
total_fact = 0
for i in range(1, typed_nmb + 1):
    for k in range(1, i + 1):
        one_item_fact *= k
    total_fact += one_item_fact
    one_item_fact = 1
print(total_fact)


#2
typed_nmb = int(input())
total_fact = 1
for i in range(typed_nmb, 1, -1):
    total_fact = total_fact * i + 1
print(total_fact)


#3
typed_nmb = int(input())
total_fact = 1
for i in range(typed_nmb, 1, -1):
    one_item_fact = factorial(i)
    total_fact += one_item_fact
print(total_fact)

