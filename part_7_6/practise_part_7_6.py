#break, continue, else
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False
        break               # останавливаем цикл если встретили делитель числа

if flag:  # эквивалентно if flag == True:
    print('Число простое')
else:
    print('Число составное')


result = 0
for i in range(10):
    num = int(input())
    if num < 0:
        break
    result += num
print(result)


num = int(input())
number = num
flag = False
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        flag = True
        break        # прерываем цикл, так как число гарантированно содержит цифру 7
    num //= 10

if flag:  # эквивалентно if flag == True:
    print('Число', number, 'содержит цифру 7')
else:
    print('Число', number, 'не содержит цифру 7')


for i in range(1, 101):
    if i == 7 or i == 17 or i == 29 or i == 78:
        continue  # переходим на следующую итерацию
    print(i)

n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Цикл завершен.')

n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Цикл завершен.')
