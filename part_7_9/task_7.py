#На вход программе подается два натуральных числа a и b (a< b).
# Напишите программу, которая находит все простые числа от a до b включительно.

#Программа должна вывести все простые числа от a до b включительно, каждое на отдельной строке.


#Примечание 1. Простое число – это натуральное число, единственными делителями которого являются только оно само и 1.
#Примечание 2. Число 1 простым не является.

a, b = int(input()), int(input())
total = 0
for i in range(a, b + 1):
    for k in range(1, i + 1):
        if i % k == 0:
            total += 1
    if total == 2:
        print(i)
    total = 0