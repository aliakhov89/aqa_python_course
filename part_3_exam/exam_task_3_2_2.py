#На вход программе подаются два целых числа, каждое на отдельной строке.
#Программа должна вывести текст в соответствии с условием - квадрат суммы и сумму квадратов

nmb_a = int(input())
nmb_b = int(input())
square_of_the_sum = (nmb_a + nmb_b) * (nmb_a + nmb_b)
sum_of_squares = (nmb_a * nmb_a) + (nmb_b * nmb_b)

print('The square of the sum of', nmb_a, 'and', nmb_b, 'is equal to', square_of_the_sum)
print('The sum of squares', nmb_a, 'and', nmb_b, 'is equal to', sum_of_squares)