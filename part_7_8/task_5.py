#Дано натуральное число n.
#Напишите программу, которая печатает численный треугольник в соответствии с примером:

#1
#22
#333
#4444
#55555
#...

#Примечание. Используйте вложенный цикл for.

typed_nmb = int(input())
for row in range(1, typed_nmb + 1):
    for row_items in range(row):
        print(row, end = '')
    print()

#for i in range(1, typed_nmb) + 1):
    #print(str(i) * i)
