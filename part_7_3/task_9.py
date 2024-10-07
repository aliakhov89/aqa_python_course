#На вход программе подается натуральное число n≥2, а затем n различных натуральных чисел последовательности,
# каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

num_n = int(input())
counter_max_1 = 0
counter_max_2 = 0
for i in range(num_n):
    num_a = int(input())
    if num_a > counter_max_1:
        counter_max_1, counter_max_2 = num_a, counter_max_1
    elif num_a > counter_max_2:
        counter_max_2 = num_a
print(counter_max_1, counter_max_2, sep='\n')