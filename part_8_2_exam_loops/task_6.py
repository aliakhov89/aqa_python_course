#Дано натуральное число. Напишите программу, которая вычисляет:
#количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречаются цифры 0 и 5 (всего суммарно).

typed_nmb = int(input())
count_3 = 0
count_last_digit = 0
count_even_digit = 0
sum_greater_than_5 = 0
product_greater_than_7 = 1
count_0_and_5 = 0
last_digit = typed_nmb % 10

while typed_nmb > 0:
    x = typed_nmb % 10
    if x == 3:
        count_3 += 1
    if x == last_digit:
        count_last_digit += 1
    if x % 2 == 0:
        count_even_digit += 1
    if x > 5:
        sum_greater_than_5 += x
    if x > 7:
        product_greater_than_7 *= x
    if x == 0 or x == 5:
        count_0_and_5 += 1
    typed_nmb //= 10

print(count_3)
print(count_last_digit)
print(count_even_digit)
print(sum_greater_than_5)
print(product_greater_than_7)
print(count_0_and_5)