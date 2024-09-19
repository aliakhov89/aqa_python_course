#На вход программе подается одно целое число – длина ребра.
#Программа должна вывести текст и числа в соответствии с условием задачи.
side_length = int(input())
volume = side_length * side_length * side_length
surface_area = 6 * (side_length * side_length)
print('Volume', '=', volume)
print('Total surface area', '=', surface_area)