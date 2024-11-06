#На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая сначала выводит все отрицательные числа, затем нули,
# а затем все положительные числа, каждое на отдельной строке.
# Числа должны быть выведены в том же порядке, в котором они были введены.

digit_amount = int(input())
negative = []
positive = []
zeros = []

for digit in range(digit_amount):
    typed_digit = int(input())
    if typed_digit == 0:
        zeros.append(typed_digit)
    elif typed_digit > 0:
        positive.append(typed_digit)
    else:
        negative.append(typed_digit)
print(*negative, sep = '\n')
print(*zeros, sep = '\n')
print(*positive, sep = '\n')