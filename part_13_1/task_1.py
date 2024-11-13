#Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10 в соответствии с образцом
#**********
#*        *
#*        *
#*        *
#*        *
#*        *
#*        *
#*        *
#*        *
#*        *
#*        *
#*        *
#*        *
#**********

def draw_box():
    for i in range(1, 15):
        if i == 1 or i == 14:
            print('**********')
        else:
            print('*        *')

draw_box()

#додав змінну width:

def draw_box():
    width = 10  # ширина строки
    for i in range(1, 15):
        if i == 1 or i == 14:
            print('*' * width)
        else:
            print('*' + ' ' * (width - 2) + '*')
draw_box()