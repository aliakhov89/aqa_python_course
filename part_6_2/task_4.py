#Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название город
#Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

city_1_name = input()
city_2_name = input()
city_3_name = input()

city_1_name_length = len(city_1_name)
city_2_name_length = len(city_2_name)
city_3_name_length = len(city_3_name)

if min(city_1_name_length, city_2_name_length, city_3_name_length) == city_1_name_length:
    print(city_1_name)
elif min(city_2_name_length, city_3_name_length) == city_2_name_length:
    print(city_2_name)
elif min(city_1_name_length, city_3_name_length) == city_3_name_length:
    print(city_3_name)
if max(city_1_name_length, city_2_name_length, city_3_name_length) == city_1_name_length:
    print(city_1_name)
elif max(city_2_name_length, city_3_name_length) == city_2_name_length:
    print(city_2_name)
elif max(city_1_name_length, city_3_name_length) == city_3_name_length:
    print(city_3_name)

