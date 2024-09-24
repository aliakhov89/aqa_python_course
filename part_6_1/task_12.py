#На вход программе подается четыре целых числа, каждое на отдельной строке – p1, p2, q1, q2
#Программа должна вывести одно число – манхэттенское расстояние.
from part_6_1.task_2 import distance

distance_p_1 = int(input())
distance_p_2 = int(input())
distance_q_1 = int(input())
distance_q_2 = int(input())

print(abs(distance_p_1 - distance_q_1) + abs(distance_p_2 - distance_q_2))