#lesson: integers
num1 = 7                # num1 - is the number
num2 = 10               # num2 - is the number
num3 = num1 + num2      # num3 - is the number
print(num3)

a = 3
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)

num1 = 2 + 3 * 4
num2 = (2 + 3) * 4

print(num1)
print(num2)

s = '1992'
year = int(s)
print(year)
aaa = 2 + year
print(aaa)

num1 = int(input())
num2 = int(input())

print(num1 + num2)

num = 17
s = str(num)

#tasks for 2.4
#1
first_number = int(input())
second_number = first_number + 1
third_number = second_number + 1
print(first_number, second_number, third_number, sep = '\n')

#2
first_number = int(input())
second_number = int(input())
third_number = int(input())
print(first_number + second_number + third_number)

#3
side_length = int(input())
V = side_length * side_length * side_length
S = 6 * (side_length * side_length)
print('Volume', '=', V)
print('Total surface area', '=', S)

#4
a = int(input())
b = int(input())
f_x = 3 * ((a + b) * (a + b) * (a + b)) + 275 * (b*b) - 127 * a -41
print(f_x)

#Следующее за числом -10 число: -9
#Для числа -10 предыдущее число: -11

#5
mid_nmb = int(input())
next_nmb = mid_nmb + 1
prev_nmb = mid_nmb - 1

print('Next number after', mid_nmb, 'is number:', next_nmb)
print('Previous number before', mid_nmb, 'is number:', prev_nmb)

#6
monitor_cost = int(input())
system_unit_cost = int(input())
keyboard_cost = int(input())
mouse_cost = int(input())
total_cost_of_one_pc = monitor_cost + system_unit_cost + keyboard_cost + mouse_cost
computers_amount = 3
print(total_cost_of_one_pc * computers_amount)

#7
a = int(input())
b = int(input())
print(a, '+', b, '=', a+b)
print(a, '-', b, '=', a-b)
print(a, '*', b, '=', a*b)

#8
a_1 = int(input())
d = int(input())
n = int(input())
a_n = a_1 + d * (n - 1)
print(a_n)

#9
x = int(input())
x_2 = x * 2
x_3 = x * 3
x_4 = x * 4
x_5 = x * 5
print(x, x_2, x_3, x_4, x_5, sep='---')