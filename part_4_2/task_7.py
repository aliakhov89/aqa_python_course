#На вход программе подаются четыре числа от 1 до 8.
#Программа должна вывести текст в соответствии с условием задачи. Ход ладьи YES or NO

current_row = int(input())
current_column = int(input())
next_row = int(input())
next_column = int(input())

if next_row == current_row or next_column == current_column:
    print("YES")
else:
    print("NO")