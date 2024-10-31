numbers = [1, 1, 2, 3, 5, 8, 13]  # создаем список

numbers.append(21)  # добавляем число 21 в конец списка
numbers.append(34)  # добавляем число 34 в конец списка

print(numbers)


numbers = [0, 2, 4, 6, 8, 10]
odds = [1, 3, 5, 7]

numbers.extend(odds)
print(numbers)


words1 = ['iq option', 'stepik', 'beegeek']
words2 = ['iq option', 'stepik', 'beegeek']

words1.append('python')
words2.extend('python')

print(words1)
print(words2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[5]    # удаляем элемент, имеющий индекс 5

print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[::2]

print(numbers)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'magenta']
del colors[2]
del colors[6]
print(colors)