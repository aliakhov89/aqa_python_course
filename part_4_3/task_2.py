#На вход программе подаются три числа (каждое на отдельной строке) – длины сторон существующего треугольника.
#Программа должна вывести на экран текст – тип треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).

side_a = int(input())
side_b = int(input())
side_c = int(input())

if side_a == side_b == side_c:
    print('Equilateral')
elif side_a == side_b or side_b == side_c or side_a == side_c:
      if side_a != side_b or side_b != side_c or side_a != side_c:
        print('Isosceles')
elif side_a != side_b != side_c:
    print('Scalene')