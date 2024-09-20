#На вход программе подаётся одно целое число – порядковый номер месяца.
#Программа должна вывести количество дней в этом месяце.

month_nmb = int(input())
if month_nmb == 2:
    print('28')
elif month_nmb == 4 or month_nmb == 6 or month_nmb == 9 or month_nmb == 11:
    print('30')
else:
    print('31')