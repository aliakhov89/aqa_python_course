#На вход программе подается строка текста, содержащая целые числа.
# Из данной строки формируется список чисел.
# Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

#Программа должна вывести одно число – количество пар элементов, равных друг другу.

typed_digits = input().split()
counter = 0
for i in range(len(typed_digits)):
    for j in range(i + 1, len(typed_digits)):
        if typed_digits[i] == typed_digits[j]:
            counter += 1
print(counter)