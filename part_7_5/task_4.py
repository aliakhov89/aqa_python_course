#Дано натуральное число.
#Напишите программу, которая вычисляет:
    #сумму его цифр;
    #количество цифр в нем;
    #произведение его цифр;
    #среднее  арифметическое его цифр;
    #его первую цифру;
    #сумму его первой и последней цифры.


num = int(input())
counter = 0
nmbs_amount = 0
nmbs_product = 1
get_last_digit = num % 10
while num != 0:
    last_digit = num % 10
    nmbs_amount += last_digit
    nmbs_product *= last_digit
    counter += 1
    first_digit = num
    num = num // 10
arithmetic_mean_of_nmbs = nmbs_amount / counter
print(nmbs_amount, counter, nmbs_product, arithmetic_mean_of_nmbs, first_digit, first_digit + get_last_digit, sep = '\n')


