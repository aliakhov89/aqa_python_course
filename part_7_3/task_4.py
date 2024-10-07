#На вход программе подается натуральное число n.
# Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно),
# квадрат которых оканчивается на 2, 5 или 8.
#Примечание. Если таких чисел нет в указанном диапазоне, то следует вывести 0


num_n = int(input())
total = 0
for i in range(1, num_n + 1):
    last_digit_sqr_i = i ** 2 % 10
    if last_digit_sqr_i == 2 or last_digit_sqr_i == 5 or last_digit_sqr_i == 8:
        total += i
print(total)
