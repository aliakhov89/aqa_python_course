numbers = [2, 4, 6, 8, 10]
languages = ['Python', 'C#', 'C++', 'Java']

print(len(numbers))      # выводим длину списка numbers
print(len(languages))    # выводим длину списка languages

print(len(['apple', 'banana', 'cherry']))   # выводим длину списка, состоящего из 3 элементов

numbers = [2, 4, 6, 8, 10]

if 2 in numbers:
    print('Список numbers содержит число 2')
else:
    print('Список numbers не содержит число 2')

print([1, 2, 3, 4] + [5, 6, 7, 8])
print([7, 8] * 3)
print([0] * 10)


numbers = [3, 4, 10, 3333, 12, -7, -5, 4]
print('Минимальный элемент =', min(numbers))
print('Максимальный элемент =', max(numbers))
