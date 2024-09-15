print(2 ** 0)
print(2 ** 1)
print(2 ** 2)
print(2 ** 3)
print(2 ** (-1))


print(2**(-2))
print((-3)**3)

print(2 ** 2 ** 3)     # 2 ** (2 ** 3) = 2 ** 8


print(10 // 3)
print(10 // 4)
print(10 // 5)
print(10 // 6)
print(10 // 12)

print(10 // 3)
print(-10 // 3)


print(10 % 3)
print(10 % 4)
print(10 % 5)
print(10 % 6)
print(10 % 12)
print(10 % 20)

print(5 % 9)
print(3 % 13)
print(5 // 9)
print(3 // 13)


print(-10**2)  # -100
print(5 * 3**2)  # 45
print((-10)**2)
print((-10)**3)

print(-123 // 10)
print(2 // 5 )

a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a)


num = 17
a = num % 10
b = num // 10
print(a)
print(b)


num = 754
a = num % 10
b = (num % 100) // 10
c = num // 100
print(a)
print(b)
print(c)


num = int(input())
last_digit = num % 10
first_digit = num // 10

print('Число десятков =', first_digit)
print('Число единиц =', last_digit)


num = int(input())
last_digit = num % 10
first_digit = num // 10

print('Сумма цифр =', last_digit + first_digit)
