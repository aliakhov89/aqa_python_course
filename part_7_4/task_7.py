#Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево.
# К тому же ведьмак не принимает купюры, он принимает только чеканные монеты.
# В мире ведьмака существуют монеты с номиналами 1,5,10,25.
#Напишите программу, которая определяет, какое минимальное количество чеканных монет нужно заплатить ведьмаку.
from part_7_4.task_6 import counter

#На вход программе подается одно натуральное число - цена за услугу ведьмака.
#Программа должна вывести минимально возможное количество чеканных монет для оплаты.
# 1,5,10,25.
# 25,10,5,1

typed_coins_amount = int(input())
counter = 0
while typed_coins_amount > 0:
    if typed_coins_amount >= 25:
        typed_coins_amount -= 25
        counter += 1
    elif typed_coins_amount >= 10:
        typed_coins_amount -= 10
        counter += 1
    elif typed_coins_amount >= 5:
        typed_coins_amount -= 5
        counter += 1
    elif typed_coins_amount >= 1:
        typed_coins_amount -= 1
        counter += 1
print(counter)


