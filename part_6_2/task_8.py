#Будем считать email адрес корректным, если в нём есть символы собачки (@) и точки (.).
# Напишите программу, проверяющую корректность email адреса.
#Программа должна вывести строку «YES», если email адрес является корректным, или «NO» в противном случае.

typed_email = input()
if '@' in typed_email and '.' in typed_email:
    print("YES")
else:
    print("NO")