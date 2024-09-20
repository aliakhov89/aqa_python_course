#На вход программе подаются четыре целых числа a1, b1, a2,b2 каждое на отдельной строке.
# Гарантируется, что a1<b1 и a2 < b2
#Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое множество».

a_1 = int(input())
b_1 = int(input())
a_2 = int(input())
b_2 = int(input())

if b_1 < a_2 or b_2 < a_1:
    print("empty set")
elif b_1 == a_2:
    print(a_2)
elif b_2 == a_1:
    print(a_1)
elif a_2 > a_1 and b_1 < b_2:
    print(a_2, b_1)
elif a_2 < a_1 and b_2 < b_1:
    print(a_1, b_2)
elif a_1 >= a_2 and b_2 >= b_1:
    print(a_1, b_1)
elif a_1 <= a_2 and b_2 <= b_1:
    print(a_2, b_2)

