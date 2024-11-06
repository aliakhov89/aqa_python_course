names = ['Gvido', 'Roman', 'Timur']
print(names)
names.insert(0, 'Anders')
print(names)
names.insert(3, 'Josef')
print(names)

names = ['Gvido', 'Roman', 'Timur']
position = names.index('Timur')
print(position)

food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
print(food)
food.remove('Рис')
print(food)

names = ['Gvido', 'Roman', 'Timur']
item = names.pop(1)
print(item)
print(names)

names = ['Gvido', 'Roman', 'Timur']
names.reverse()
print(names)


names = ['Gvido', 'Roman', 'Timur']
names.clear()
print(names)

names = ['Gvido', 'Roman', 'Timur']
names_copy = names.copy()              # создаем поверхностную копию списка names
print(names)
print(names_copy)


names = ['Gvido', 'Roman', 'Timur']
names_copy1 = list(names)             # создаем поверхностную копию с помощью функции list()
names_copy2 = names[:]