#Дано натуральное число n(n≥10).
#Напишите программу, которая определяет его максимальную и минимальную цифры и выводит текст в следующем формате:
#Максимальная цифра равна <максимальная цифра>
#Минимальная цифра равна <минимальная цифра>

num = int(input())
min_num = 9
max_num = 0
while num != 0:
    last_number = num % 10
    if last_number >= max_num:
        max_num = last_number
    if last_number <= min_num:
        min_num = last_number
    num //= 10
print('Maximum digit is equal to', max_num)
print('Minimum digit is equal to', min_num)

