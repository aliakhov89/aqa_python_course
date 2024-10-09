#Дано натуральное число.
#Напишите программу, которая вычисляет:
    #сумму его цифр;
    #количество цифр в нем;
    #произведение его цифр;
    #среднее  арифметическое его цифр;
    #его первую цифру;
    #сумму его первой и последней цифры.


num = int(input())
nmbs_sum = 0
nmbs_amount = 0
nmbs_product = 1
get_last_digit = num % 10
while num != 0:
    last_digit = num % 10
    nmbs_sum += last_digit
    nmbs_product *= last_digit
    nmbs_amount += 1
    first_digit = num
    num = num // 10
arithmetic_mean_of_nmbs = nmbs_sum / nmbs_amount
print(nmbs_sum, nmbs_amount, nmbs_product, arithmetic_mean_of_nmbs, first_digit, first_digit + get_last_digit, sep = '\n')


