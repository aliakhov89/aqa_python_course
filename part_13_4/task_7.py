#На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания.
# Из данных строк формируются списки чисел.
# Напишите программу, которая объединяет указанные списки в один отсортированный список с помощью функции quick_merge(), а затем выводит его.
from part_7_6.practise_part_7_6 import result


#Формат входных данных
#На вход программе подается натуральное число n, а затем n строк, содержащих целые числа в порядке возрастания, разделенные символом пробела.

#Формат выходных данных
#Программа должна вывести элементы окончательного отсортированного списка каждое через пробел.

def quick_merge(list_1, list_2):
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

list_1 = []
for i in range(int(input())):
    list_2 = [int(j) for j in input().split()]
    result = quick_merge(list_1, list_2)
    list_1 = result
print(*result)


