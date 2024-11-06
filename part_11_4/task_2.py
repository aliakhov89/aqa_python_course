#На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая для каждого введенного числа x выводит значение функции f(x)=x**2 + 2x+1, каждое на отдельной строке.

digit_amount = int(input())
digits = []
for digit in range(digit_amount):
    digits.append(int(input()))
print(*digits, sep = '\n')
print()
for x in digits:
    print( x ** 2 + 2 * x + 1)



x = [int(input()) for i in range(int(input()))]
print(*x, sep='\n')
print()
for num in x:
    print(num ** 2 + 2 * num + 1)
