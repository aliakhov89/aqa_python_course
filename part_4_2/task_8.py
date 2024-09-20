#На вход программе подаются четыре числа от 1 до 8.
#Программа должна вывести текст в соответствии с условием задачи. Ход короля YES or NO

current_row = int(input())
current_column = int(input())
next_row = int(input())
next_column = int(input())

if (next_row == (current_row + 1) or next_row ==(current_row - 1) or next_row == current_row) and (next_column == (current_column + 1) or next_column ==(current_column - 1) or next_column == current_column):
    print("YES")
else:
    print("NO")