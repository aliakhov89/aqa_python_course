#На вход программе подаются две строки, каждая на отдельной строке.Красный, синий и желтый
#Программа должна вывести полученный цвет смешения либо сообщение «ошибка цвета», если введён был не цвет.

first_color = input()
second_color = input()

if (first_color == 'red' or second_color == 'red') and (first_color == 'blue' or second_color == 'blue'):
        print('purple')
elif (first_color == 'yellow' or second_color == 'yellow') and (first_color == 'red' or second_color == 'red'):
        print('orange')
elif (first_color == 'blue' or second_color == 'blue') and (first_color == 'yellow' or second_color == 'yellow'):
        print('green')
elif first_color == second_color and (first_color == 'blue' or first_color == 'red' or second_color == 'yellow'):
        print(first_color)
else:
    print('color error')