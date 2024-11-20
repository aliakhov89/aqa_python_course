#Напишите функцию merge(list1, list2),
# которая принимает в качестве аргументов два отсортированных по возрастанию списка,
# состоящих из целых чисел, и объединяет их в один отсортированный список.

#Примечание 1. Списки list1 и list2 могут иметь разную длину.

#Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него. 😎

def merge(list_1, list_2):
    result = []
    index_list_1 = 0
    index_list_2 = 0
    while index_list_1 < len(list_1) and index_list_2 < len(list_2):
        if list_1[index_list_1] <= list_2[index_list_2]:
            result.append(list_1[index_list_1])
            index_list_1 += 1
        else:
            result.append(list_2[index_list_2])
            index_list_2 += 1
    if index_list_1 < len(list_1):
        result += list_1[index_list_1:]
    elif index_list_2 < len(list_2):
        result += list_2[index_list_2:]
    return result


numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))