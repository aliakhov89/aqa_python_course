#На вход программе подаются три различных целых числа, каждое на отдельной строке.
#Программа должна вывести серединное значение из набора трёх чисел.

first_nmb = int(input())
second_nmb = int(input())
third_nmb = int(input())

if first_nmb < second_nmb < third_nmb:
    print(second_nmb)
elif first_nmb < third_nmb < second_nmb:
    print(third_nmb)
elif first_nmb > second_nmb > third_nmb:
    print(second_nmb)
elif second_nmb > first_nmb > third_nmb:
    print(first_nmb)
elif first_nmb > third_nmb > second_nmb:
    print(third_nmb)
elif second_nmb < first_nmb < third_nmb:
    print(first_nmb)