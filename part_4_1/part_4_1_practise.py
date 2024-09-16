#if
answer = input('What programming language are we learning?')
if answer == 'Python':
    print('Right! We learning Python =)')
    print('Python is a great programming language!')

#if else
answer = input('What programming language are we learning?')

if answer == 'Python':
    print('Right! We learning Python =)')
    print('Python is a great programming language!')
else:
    print('Not exactly!')

# ==
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 < num2:
    print(num1, 'less than', num2)
if num1 > num2:
    print(num1, 'more than', num2)

if num1 == num2:  # используем двойное равенство
    print(num1, 'equal', num2)
if num1 != num2:
    print(num1, 'not equal', num2)

if num1 == num2 == num3:
    print('All three numbers are equal')

age = int(input())
if 3 <= age <= 6:
    print('You are a child')
else:
    print('You are not a child')