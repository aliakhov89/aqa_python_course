#На вход программе подаётся натуральное число n.
#Напишите программу вычисления знакочередующейся суммы:

num_n = int(input())
total = 0
for i in range(1, num_n + 1):
    if i % 2 == 0:
        total -= i
    else:
        total += i
print(total)