#На вход программе подается строка текста, содержащая натуральные числа.
# Напишите программу, которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.
#Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела.
#Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

typed_nmbs = [int(i) for i in input().split()]
print(*typed_nmbs, sep = '+', end = '')
print('=', sum(typed_nmbs), sep = '')
