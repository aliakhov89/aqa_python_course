#Напишите программу, которая упорядочивает три числа от большего к меньшему.
#На вход программе подаются три целых числа, каждое на отдельной строке.
#Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.


nmb_1 = int(input())
nmb_2 = int(input())
nmb_3 = int(input())
max_nmb = max(nmb_1, nmb_2, nmb_3)
min_nmb = min(nmb_1, nmb_2, nmb_3)
mid_nmb = (nmb_1 + nmb_2 + nmb_3) - max_nmb - min_nmb

print(max_nmb, mid_nmb, min_nmb, sep = '\n')