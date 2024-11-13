#На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел.
# Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию.

#Формат входных данных
#На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.

#Формат выходных данных
#Программа должна вывести две строки текста в соответствии с условием задачи.

typed_nmbs = input().split()
for nmb in range(len(typed_nmbs)):
    typed_nmbs[nmb] = int(typed_nmbs[nmb])
typed_nmbs.sort()
print(*typed_nmbs)
typed_nmbs.sort(reverse = True)
print(*typed_nmbs)


#2
typed_nmbs = list(map(int, input().split()))
print(*sorted(typed_nmbs))
print(*sorted(typed_nmbs, reverse=True))