#На вход программе подаётся одно целое число.
#Программа должна вывести текст в соответствии с условием задачи.
#Следующее за числом <текущее число> число: <следующее число>
#Для числа <текущее число> предыдущее число: <предыдущее число>
mid_nmb = int(input())
next_nmb = mid_nmb + 1
prev_nmb = mid_nmb - 1

print('Next number after', mid_nmb, 'is number:', next_nmb)
print('Previous number before', mid_nmb, 'is number:', prev_nmb)