numbers = [0, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(numbers)):
    print(numbers[i])


numbers = [0, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num, end=' ')


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*numbers, sep='\n')

s = 'Python'
print(*s)
print()
print(*s, sep='\n')