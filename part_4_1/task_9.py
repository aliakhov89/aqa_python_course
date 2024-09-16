#На вход программе подаются три целых числа, каждое на новой строке.
#Программа должна вывести одно число – сумму положительных чисел
nmb_1 = int(input())
nmb_2 = int(input())
nmb_3 = int(input())

sum_of_3_nmb = 0

if nmb_1 > 0:
    sum_of_3_nmb = sum_of_3_nmb + nmb_1
if nmb_2 > 0:
    sum_of_3_nmb = sum_of_3_nmb + nmb_2
if nmb_3 > 0:
    sum_of_3_nmb = sum_of_3_nmb + nmb_3
print(sum_of_3_nmb)


