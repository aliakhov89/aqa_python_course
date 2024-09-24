#На вход программе подаются два целых числа n и k – скорости Зума и Флэша.
#Если Зум быстрее Флэша, нужно вывести «NO», а если Флэш быстрее Зума, нужно вывести «YES».
# В случае же если их скорости равны, нужно вывести «Don't know».

zoom_speed = int(input())
flash_speed = int(input())
if zoom_speed > flash_speed:
    print("NO")
elif zoom_speed < flash_speed:
    print("YES")
else:
    print("Don't know")