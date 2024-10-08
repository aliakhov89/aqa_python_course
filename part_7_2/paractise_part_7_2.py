#Цикл for: функция range

for i in range(100, 1000):  # перебираем числа от 100 до 999
    if i % 10 == 7:         # используем остаток от деления на 10, для получения последней цифры
        print(i)

for i in range(56, 171, 2):
    print(i)

for i in range(5, 0, -1):
    print(i, end=' ')
print('Starts!!!')