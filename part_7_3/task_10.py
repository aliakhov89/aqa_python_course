#Напишите программу, которая считывает последовательность из 10 целых чисел
# и определяет, является ли каждое из них чётным или нет.
#Программа должна вывести текст «YES» (без кавычек), если все числа чётные, или «NO» (без кавычек) в противном случае.
flag = True
for i in range(10):
    num_a = int(input())
    if num_a % 2 != 0:
        flag = False
if flag:
    print('YES')
else:
    print('NO')