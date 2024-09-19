#На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.
#Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа, в следующем порядке (каждое на новой строке abc, acb, bac, bca, cab, cba

input_number = int(input())
digit1 = input_number // 100
digit2 = (input_number // 10) % 10
digit3 = input_number % 10
print(digit1, digit2, digit3, sep = '', end='\n' )
print(digit1, digit3, digit2, sep = '', end='\n' )
print(digit2, digit1, digit3,  sep = '', end='\n' )
print(digit2, digit3, digit1, sep = '', end='\n' )
print(digit3, digit1, digit2, sep = '', end='\n' )
print(digit3, digit2, digit1, sep = '', end='\n' )