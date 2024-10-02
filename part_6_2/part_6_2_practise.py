s1 = 'Python rocks!'
s2 = "Python rocks!"

s3 = 'abcdef'
length1 = len(s3)               # считаем длину строки из переменной s1
length2 = len('Python rocks!')  # считаем длину строкового литерала
print(length1)
print(length2)

num1 = 1777    # целое число
num2 = 17.77   # число с плавающей точкой
s1 = str(num1) # преобразовали целое число в строку '1777'
s2 = str(num2) # преобразовали число с плавающей точкой в строку '17.77'

s1 = 'ab' + 'bc'
s2 = 'bc' + 'ab'
s3 = s1 + s2 + '!!'
print(s1)
print(s2)
print(s3)