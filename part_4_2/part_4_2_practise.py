num = int(input())
if 100 <= num <= 999:     # num >= 100 and num <= 999
    print('Число является трёхзначным')
else:
    print('Число не является трёхзначным')

num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1:
    print('Цифры различны')
else:
    print('Цифры не различны')


x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')

num1 = 34
num2 = 81
if num1 // 9 == 0 or num2 % 9 == 0:
    print('число', num1, 'выиграло')
else:
    print('число', num2, 'выиграло')

a = int(input())

if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5

p = (a + b) * (a + b)
print(p)