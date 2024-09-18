#На вход программе подаются четыре строки (каждая на отдельной строке): строка-разделитель и три строки.
#Программа должна вывести введённые три строки через разделитель.
separator = input()
second_raw = input()
third_raw = input()
fourth_raw = input()
print(second_raw, third_raw, fourth_raw, sep=separator)