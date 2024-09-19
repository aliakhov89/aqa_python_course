#На вход программе подаётся положительное трёхзначное число.
#Программа должна вывести текст в соответствии с условием задачи.

input_number = int(input())

digit1 = input_number // 100
digit2 = (input_number // 10) % 10
digit3 = input_number % 10
digits_summ = digit1 + digit2 + digit3
digits_product = digit1 * digit2 * digit3

print('Sum of digits', '=', digits_summ)
print('Product of digits', '=', digits_product)
