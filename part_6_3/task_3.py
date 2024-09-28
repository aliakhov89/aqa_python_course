#На вход программе подается два вещественных числа a и b
#Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

import math

num_a = float(input())
num_b = float(input())

arithmetic_mean_of_nmbs = (num_a + num_b) / 2
geometric_mean_of_nmbs = math.sqrt(num_a * num_b)
harmonic_mean_of_nmbs = 2*num_a*num_b / (num_a + num_b)
mean_square_of_nmbs = math.sqrt((math.pow(num_a, 2) + math.pow(num_b, 2)) / 2)

print(arithmetic_mean_of_nmbs, geometric_mean_of_nmbs, harmonic_mean_of_nmbs, mean_square_of_nmbs, sep='\n')