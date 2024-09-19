#На вход программе подаётся целое число – количество минут.
#Программа должна вывести текст в соответствии с условием задачи.

#<исходное кол-во минут> мин - это <полное кол-во часов> час <оставшееся кол-во минут> минут.

minutes_amount = int(input())
hours_amount = minutes_amount // 60
remains_minutes = minutes_amount % 60

print(minutes_amount, 'is', hours_amount, 'hours', remains_minutes, 'minutes.')

