#На вход программе подается пять целых чисел, каждое на отдельной строке.
#Программа должна вывести наименьшее и наибольшее число с поясняющей надписью.

nmb_1 = int(input())
nmb_2 = int(input())
nmb_3 = int(input())
nmb_4 = int(input())
nmb_5 = int(input())

print("min number", "=", min(nmb_1, nmb_2, nmb_3, nmb_4, nmb_5))
print("max number", "=", max(nmb_1, nmb_2, nmb_3, nmb_4, nmb_5))