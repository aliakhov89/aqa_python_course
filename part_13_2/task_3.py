#Напишите функцию print_digit_sum(), которая принимает одно натуральное число num и выводит на печать сумму его цифр.

typed_nmbs = int(input())

def print_digit_sum(typed_nmbs):
    sum_of_mnbs = 0
    while typed_nmbs > 0:
        sum_of_mnbs += typed_nmbs % 10
        typed_nmbs //= 10
    print(sum_of_mnbs)

print_digit_sum(typed_nmbs)

