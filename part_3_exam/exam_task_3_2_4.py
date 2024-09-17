#На вход программе подаётся одно целое положительное число n
#Программа должна вывести число n + nn + nnn

nmb_n = int(input())
#convert int to str
nmb_n_in_string = str(nmb_n)
#concatenate strings
nmb_n_in_string_2_digits = nmb_n_in_string + nmb_n_in_string
nmb_n_in_string_3_digits = nmb_n_in_string + nmb_n_in_string + nmb_n_in_string
#convert str to int
nmb_n_2_digits = int(nmb_n_in_string_2_digits)
nmb_n_3_digits = int(nmb_n_in_string_3_digits)
#summ of strings
sum_of_1_2_3_digits_n = nmb_n + nmb_n_2_digits + nmb_n_3_digits
print(sum_of_1_2_3_digits_n)

