def draw_box(height, width):    # функция принимает два параметра
    for i in range(height):
        print('*' * width)

draw_box(4, 10)


draw_box(3, 3)
print()
draw_box(5, 5)
print()
draw_box(4, 10)



def draw_box(height, width):
    height = 2
    width = 10
    for i in range(height):
        print('*' * width)

n = 5
m = 7
draw_box(n, m)
print(n, m)

