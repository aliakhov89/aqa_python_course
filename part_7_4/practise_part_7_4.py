#while
i = 0
while i < 10:
    print('Привет')
    i += 1

num = int(input())
while num != -1:
    print('Квадрат вашего числа равен:', num * num)
    num = int(input())


# используем for
for i in range(101):
    print(i)

# используем while
i = 0
while i < 101:
    print(i)
    i += 1

text = input()
total = 0
while text != 'stop':
    total += int(text)
    text = input()

print('Сумма чисел равна', total)
