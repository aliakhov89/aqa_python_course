#На вход программе подаётся два целых числа: количество школьников и количество мандаринов, каждое на отдельной строке.
#Программа должна вывести два числа: количество мандаринов, которое достанется каждому школьнику, и количество мандаринов, которое останется в корзине, каждое на отдельной строке.

schoolboy_amount = int(input())
tangerine_amount = int(input())

tangerine_for_schoolboy = tangerine_amount // schoolboy_amount
tangerine_remains = tangerine_amount % schoolboy_amount

print(tangerine_for_schoolboy)
print(tangerine_remains)