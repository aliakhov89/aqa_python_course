#На вход программе подаются четыре целых положительных числа a,b,c и d, каждое на отдельной строке.
#Программа должна вывести значение a в степени b + c в степени d
nmb_a = int(input())
nmb_b = int(input())
nmb_c = int(input())
nmb_d = int(input())
nmb_a_in_b = nmb_a ** nmb_b
nmb_c_in_d = nmb_c ** nmb_d
sum_of_degrees = nmb_a_in_b + nmb_c_in_d
print(sum_of_degrees)
