#При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение.
#На вход программе подается натуральное число n, а затем n различных натуральных чисел.
# Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел,
# а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.




digit_amount = int(input())
digits = []
for digit in range(digit_amount):
    digits.append(int(input()))
del digits[digits.index(max(digits))]
del digits[digits.index(min(digits))]
print(*digits, sep = '\n')