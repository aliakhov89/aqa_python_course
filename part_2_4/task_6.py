#На вход программе подаются четыре целых числа (каждое на отдельной строке):
#стоимость монитора, стоимость системного блока, стоимость клавиатуры, стоимость мыши.
#Программа должна вывести одно число – стоимость покупки (трёх компьютеров).
monitor_cost = int(input())
system_unit_cost = int(input())
keyboard_cost = int(input())
mouse_cost = int(input())
total_cost_of_one_pc = monitor_cost + system_unit_cost + keyboard_cost + mouse_cost
computers_amount = 3
print(total_cost_of_one_pc * computers_amount)