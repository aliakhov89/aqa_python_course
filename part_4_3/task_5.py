#На вход программе подаётся одно целое число. - вес боксера-любителя
#Программа должна вывести текст – название весовой категории.
boxer_weight = int(input())
if boxer_weight < 60:
    print('Light weight')
elif 60 <= boxer_weight < 64:
    print('First Welterweight')
elif 64 <= boxer_weight < 69:
    print('Welterweight')