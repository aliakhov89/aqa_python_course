#На вход программе подаётся положительное четырёхзначное целое число.
#Программа должна вывести текст в соответствии с условием задачи.

input_number = int(input())
digit1 = input_number // 1000
digit2 = input_number // 100 % 10
digit3 = input_number  // 10 % 10
digit4 = input_number // 1 % 10

print('The digit in the thousands position is equal to', digit1)
print('The digit in the hundreds position is equal to', digit2)
print('The digit in the tens position is equal to', digit3)
print('The digit in the units position is equal to', digit4)

