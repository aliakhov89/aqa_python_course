#На вход программе подаются три целых числа b1, q, n каждое на отдельной строке.
#Программа должна вывести  n-й член геометрической прогрессии.

numb_b_1 = int(input())
numb_q = int(input())
numb_n = int(input())

numb_b_n = numb_b_1 * numb_q ** (numb_n - 1)
print(numb_b_n)

