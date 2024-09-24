#На вход программе подаются два целых числа и строка, все на отдельной строке. (+, -, *, /)
#Программа должна вывести результат применения операции к введенным числам или соответствующий текст,
# если операция неверная либо если происходит деление на ноль.

first_nmb = int(input())
second_nmb = int(input())
math_operation = input()

if math_operation == '+':
    print(first_nmb + second_nmb)
elif math_operation == '-':
    print(first_nmb - second_nmb)
elif math_operation == '*':
    print(first_nmb * second_nmb)
elif math_operation == '/':
      if second_nmb == 0:
        print("You can't divide by zero!")
      else: print(first_nmb / second_nmb)
else:
    print('Invalid operation')