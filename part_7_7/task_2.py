#На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке).
# Известно, что вводимые числа по абсолютной величине не превышают 10 в 6 степени
# Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел последовательности и максимальное отрицательное число в последовательности.
# Если отрицательных чисел нет, требуется вывести на экран «NO» (без кавычек). Программист торопился и написал программу неправильно.

#Найдите все ошибки в этой программе (их ровно 5).
# Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.

mx = 0 #should be more than 10 ** 6(-10000000)
s = 0
for i in range(11): #should be range(10)
    x = int(input())
    if x < 0:
        s = x #should be s += x
        if x > mx: #shift if to the right
            mx = x ##shift to the right
#I added this part
if s == 0:
    print('NO')
#I added this part
else: #added else
    print(s)
    print(mx)