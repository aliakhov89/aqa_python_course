#Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название город
#Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

city_1_name = input()
city_2_name = input()
city_3_name = input()

print(min(city_1_name, city_2_name, city_3_name, key=len), max(city_1_name, city_2_name, city_3_name, key=len), sep = '\n')



