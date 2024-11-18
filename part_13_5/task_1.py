#Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа,
#и возвращает значение True, если существует невырожденный треугольник со сторонами side1, side2, side3, или False в противном случае.

#Примечание 1. С данной задачей мы уже сталкивались при изучении условного оператора.

def is_valid_triangle(side_1, side_2, side_3):
    if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
        return True
    return False

a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))