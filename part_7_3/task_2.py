#На вход программе подается натуральное числоn, а затем n целых чисел, каждое на отдельной строке.
# Напишите программу, которая подсчитывает сумму введенных чисел (не включая само числоn).

num_n = int(input())
counter = 0
for i in range(num_n):
    num_a = int(input())
    counter = counter + num_a
print(counter)