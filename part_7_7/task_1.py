#На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке).
# Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности и их произведение.
# Если неотрицательных чисел нет, требуется вывести на экран «NO».
# Программист торопился и написал программу неправильно.

#Найдите все ошибки в этой программе (их ровно 4).
# Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.

#Примечание. При необходимости вы можете добавить необходимые строки кода.

count = 0
p = 0 #should be p = 1
for i in range(1, 10): #shoud be range(1, 11) or range(10)
    x = int(input())
    if x > 0: #should be x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    print(x)  #should be print(count)
    print(p)
else:
    print('NO')